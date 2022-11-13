"""
@Author: Liang
@Time: 2022/11/13 17:06
@Github: https://github.com/Liangwe
@FileName: prod.py
@Desc: xxx
"""
from config.base import BaseConfig


class Config(BaseConfig):
    ENV = 'prod'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liang@127.0.0.1:3306/sweetmoon'
