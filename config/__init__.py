"""
@Author: Liang
@Time: 2022/11/13 17:04
@Github: https://github.com/Liangwe
@FileName: __init__.py
@Desc: xxx
"""
import importlib
import os

env = os.environ.get('ENV', 'development')
setting = importlib.import_module(f"config.{env}")
Config = setting.Config
