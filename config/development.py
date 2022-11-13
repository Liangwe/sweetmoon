"""
@Author: Liang
@Time: 2022/11/13 17:04
@Github: https://github.com/Liangwe
@FileName: development.py
@Desc: xxx
"""
from config.base import BaseConfig


class Config(BaseConfig):
    ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liang@127.0.0.1:3306/sweetmoon'
