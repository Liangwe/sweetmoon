#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Liang
@Time: 2022/5/15 21:31
@Github: https://github.com/Liangwe
@FileName: fied_methos.py
@Desc: xxx
"""
import datetime
import time

from django.db import models

from backend.sweetmoon_django.sweetmoon.settings import ALL
from backend.sweetmoon_django.utils.common import get_cls_attributes


class CustomInteger(models.IntegerField):
    def __init__(self, blank=False, default=None, max_length=None, **kwargs):
        """
        :param null:
        :param blank:
        :param kwargs:
        """
        super(CustomInteger, self).__init__(**kwargs)
        self.blank, self.default, self.max_length = blank, default, max_length
        self.null = True

    def db_type(self, connection):
        if self.max_length:
            typ = ['int(%d)' % self.max_length]
        else:
            typ = ['int(11)']
        if self.default:
            typ += ['NULL default %d' % int(self.default)]
        return ' '.join(typ)


class CustomCharField(models.CharField):
    def __init__(self, blank=False, default=None, max_length=None, **kwargs):
        """
        :param null:
        :param blank:
        :param kwargs:
        """
        super(CustomCharField, self).__init__(**kwargs)
        self.blank, self.default, self.max_length = blank, default, max_length
        self.null = True

    def db_type(self, connection):
        if self.max_length:
            typ = ['varchar(%d)' % self.max_length]
        else:
            typ = ['varchar(255)']
        if self.default:
            typ += ['NULL default "%s"' % str(self.default)]
        return ' '.join(typ)


class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """

    def __init__(self, null=False, blank=False, **kwargs):
        """
        :param null:
        :param blank:
        :param kwargs:
        """
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True  # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ = ['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL default CURRENT_TIMESTAMP']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        if isinstance(value, int):
            return datetime.datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        return time.strftime('%Y%m%d%H%M%S', value.timetuple())


def serialized_time_filed(cls, fields):
    if fields == ALL:
        fields = get_cls_attributes(cls)
    res = []
    for key in fields:
        if key.endswith("_time"):
            res.append(key)
    return res
