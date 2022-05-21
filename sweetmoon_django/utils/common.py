#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Liang
@Time: 2022/5/15 18:00
@Github: https://github.com/Liangwe
@FileName: common.py
"""
import datetime
import json

from backend.sweetmoon_django.sweetmoon.settings import DEFAULT_TIME_STR, DEFAULT_DATE_STR


class DatetimeSerializer(json.JSONEncoder):
    """
    实现 date 和 datetime 类型的 JSON 序列化
    用法: json.dumps(dict_data, cls=DatetimeSerializer)
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(DEFAULT_TIME_STR)
        elif isinstance(obj, datetime.date):
            return obj.strftime(DEFAULT_DATE_STR)
        return json.JSONEncoder.default(self, obj)


class TypeConversion:
    """
    Common conversion correlation functions
    """

    # Data type related
    @staticmethod
    def dict2json(dict_data):
        return json.dumps(dict_data, cls=DatetimeSerializer)

    @staticmethod
    def json2dict(json_str):
        return json.loads(json_str)

    @staticmethod
    def datetime_to_str(x, format_str=DEFAULT_TIME_STR):
        if isinstance(x, datetime.datetime):
            return x.strftime(format_str)
        else:
            return x

    @staticmethod
    def str_to_datetime(x, format_str=DEFAULT_TIME_STR):
        if isinstance(x, str):
            return datetime.datetime.strptime(x, format_str)
        else:
            return x


def get_cls_attributes(cls, exclude_methods=True):
    """
    拿到类中除了自定义的方法之外的 元素
    :param cls:
    :param exclude_methods: exclude native methods
    :return:
    """
    base_attrs = dir(type('dummy', (object,), {}))
    this_cls_attrs = dir(cls)
    res = []
    for attr in this_cls_attrs:
        if base_attrs.count(attr) or (callable(getattr(cls, attr)) and exclude_methods):
            continue
        else:
            res.append(attr)
    return res


if __name__ == '__main__':
    pass
