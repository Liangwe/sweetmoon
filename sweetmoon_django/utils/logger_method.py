#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Liang
@Time: 2022/5/15 21:37
@Github: https://github.com/Liangwe
@FileName: logger_method.py
@Desc: Py logger base
"""
import loguru


# TODO add some log func
class LogHandler:

    def __new__(cls, *args, **kwargs):
        return loguru.logger


logger = LogHandler()
