"""
@Author: Liang
@Time: 2022/11/13 17:39
@Github: https://github.com/Liangwe
@FileName: log_service.py
@Desc: xxx
"""
import loguru


class LogHandler:

    def __new__(cls, *args, **kwargs):
        return loguru.logger


logger = LogHandler()
