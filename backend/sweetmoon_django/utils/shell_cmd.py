#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Liang
@Time: 2022/5/15 21:34
@Github: https://github.com/Liangwe
@FileName: shell_cmd.py
@Desc: xxx
"""
import subprocess


class ShellCmd(object):
    def __init__(self):
        pass

    def run_cmd(self, cmd):
        """
        :param cmd: shell cmd
        :return: {'ret': <ret>, 'stdout': <stdout>, 'stderr': <stderr}
        """
        p = subprocess.Popen(
            cmd,
            shell=True,
            universal_newlines=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        try:
            (stdout, stderr) = p.communicate()
        except Exception as e:
            p.kill()
            (stdout, stderr) = p.communicate()
        ret = p.returncode
        return {'ret': ret, 'stdout': stdout, 'stderr': stderr}