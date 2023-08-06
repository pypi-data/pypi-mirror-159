#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedhf\api\serial\deserializer.py
# @Time    :   2022-05-03 15:59:24
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

import io
import torch


class Deserializer(object):
    """
    Deserializer
    """

    @staticmethod
    def deserialize_model(
        model: torch.nn.Module, serialized_parameters: torch.Tensor, mode="copy"
    ):
        cur_idx = 0
        for parameter in model.parameters():
            numel = parameter.data.numel()
            size = parameter.data.size()
            if mode == "copy":
                parameter.data.copy_(
                    serialized_parameters[cur_idx : cur_idx + numel].view(size)
                )
            elif mode == "add":
                parameter.data.add_(
                    serialized_parameters[cur_idx : cur_idx + numel].view(size)
                )
            else:
                raise ValueError("Unknown mode: {}".format(mode))
            cur_idx += numel
