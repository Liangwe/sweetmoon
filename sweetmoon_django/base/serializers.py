#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Liang
@Time: 2022/5/15 21:30
@Github: https://github.com/Liangwe
@FileName: serializers.py.py
@Desc: xxx
"""
from sweetmoon_django.base.models import UserInfo
from sweetmoon_django.sweetmoon.settings import ALL
from sweetmoon_django.utils.field_methods import serialized_time_filed
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    """
    序列化创建
    key = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    """
    class Meta:
        model = UserInfo
        fields = ALL

    time_fields = serialized_time_filed(Meta.model, Meta.fields)
    if time_fields:
        for i in time_fields:
            locals()[i] = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")



