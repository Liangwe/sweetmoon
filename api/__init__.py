"""
@Author: Liang
@Time: 2022/11/12 21:49
@Github: https://github.com/Liangwe
@FileName: __init__.py
@Desc: xxx
"""
from utils.tools import NestableBlueprint

api_blue = NestableBlueprint(
    'api', __name__, url_prefix='/api'
)
