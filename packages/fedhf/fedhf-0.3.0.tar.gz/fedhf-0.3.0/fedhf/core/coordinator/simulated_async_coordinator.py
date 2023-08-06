#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedhf\core\coordinator\simulated_async_coordinator.py
# @Time    :   2022-05-03 16:02:37
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from copy import deepcopy
import os

import numpy as np

from fedhf.core import build_client

from .base_coordinator import SimulatedBaseCoordinator


class SimulatedAsyncCoordinator(SimulatedBaseCoordinator):
    """Simulated Coordinator
    In simulated scheme, the data and model belong to coordinator and there is no need communicator.
    Also, there is no need to instantiate every client.
    """

    def __init__(self, args) -> None:
        super(SimulatedAsyncCoordinator, self).__init__(args)

    def prepare(self) -> None:
        super(SimulatedAsyncCoordinator, self).prepare()

        assert self.args.deploy_mode == "simulated"
        self._model_queue = []
        self._last_update_time = {client_id: 0 for client_id in self.client_list}

    def main(self) -> None:
        try:
            self.max_staleness = self.args[self.args.algor].get("max_staleness", 16)
            self._model_queue.append(deepcopy(self.server.model))

            for i in range(self.args.num_rounds):
                # self.logger.info(f'{self.server.model.get_model_version()}')

                selected_clients = self.server.select(self.client_list)

                self.logger.info(f"Round {i} Selected clients: {selected_clients}")

                for client_id in selected_clients:
                    client = build_client(self.args.deploy_mode)(
                        self.args, client_id, data_size=len(self.data[client_id])
                    )

                    staleness = np.random.randint(
                        low=1,
                        high=min(
                            self.max_staleness,
                            max(self.server.model.get_model_version(), 0) + 1,
                            self.server.model.get_model_version()
                            - self._last_update_time[client_id]
                            + 1,
                        )
                        + 1,
                    )

                    assert (
                        staleness <= max(0, self.server.model.get_model_version()) + 1
                    )
                    assert staleness <= len(self._model_queue)
                    assert (
                        staleness
                        <= self.server.model.get_model_version()
                        - self._last_update_time[client_id]
                        + 1
                    )

                    self.logger.info(
                        f"Client {client_id} staleness: {staleness} start train from model version : {self._model_queue[-staleness].get_model_version()}"
                    )

                    model, result = client.train(
                        data=self.data[client_id],
                        model=deepcopy(self._model_queue[-staleness]),
                    )

                    self.server.update(
                        model,
                        server_model_version=max(
                            0, self.server.model.get_model_version()
                        ),
                        client_model_version=max(0, model.get_model_version()),
                    )

                    result = self.server.evaluate(self.dataset.testset)
                    self.logger.info(
                        f"Server model version {self.server.model.get_model_version()} result: {result}"
                    )
                    if (
                        self.server.model.get_model_version() % self.args.chkp_interval
                        == 0
                    ):
                        self.logger.info(
                            f"Save model: {self.args.exp_name}-{self.server.model.get_model_version()}.pth"
                        )
                        self.server.model.save(
                            os.path.join(
                                self.args.save_dir,
                                f"{self.args.exp_name}-{self.server.model.get_model_version()}.pth",
                            )
                        )

                    self._model_queue.append(deepcopy(self.server.model))
                    self._last_update_time[
                        client_id
                    ] = self.server.model.get_model_version()

                    while len(self._model_queue) > self.max_staleness + 1:
                        self._model_queue.pop(0)
            self.logger.info(f"All rounds finished.")

        except KeyboardInterrupt:
            self.server.model.save()
            self.logger.info(f"Interrupted by user.")

    def finish(self) -> None:
        super(SimulatedAsyncCoordinator, self).finish()

    def run(self) -> None:
        self.prepare()
        self.main()
        self.finish()
