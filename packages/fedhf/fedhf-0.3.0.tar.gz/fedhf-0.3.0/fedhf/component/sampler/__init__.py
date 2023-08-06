#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedhf\component\sampler\__init__.py
# @Time    :   2022-05-03 16:00:35
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

__all__ = [
    "build_sampler",
    "RandomSampler",
    "NonIIDSampler",
    "sampler_factory",
    "BaseSampler",
]

from .base_sampler import BaseSampler

from .random_sampler import RandomSampler
from .noniid_sampler import NonIIDSampler

sampler_factory = {
    "random": RandomSampler,
    "non-iid": NonIIDSampler,
}


def build_sampler(sam_name: str):
    if sam_name not in sampler_factory.keys():
        raise ValueError(f"Sampler {sam_name} not found.")

    sampler = sampler_factory[sam_name]

    return sampler
