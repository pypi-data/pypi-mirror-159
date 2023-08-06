#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   time_.py
@Time    :   2022/07/13 16:54:59
@Author  :   Desire
@Version :   1.0
@Desc    :   时间操作
"""


import os
import sys

sys.path.insert(1, os.getcwd())
# here put the import lib

__all__ = ["TimeTools"]

import time
from datetime import datetime


class TimeTools(object):

    @staticmethod
    def is_within_time_range(start="00:00", end="09:00") -> bool:
        """判断当前时间是否在指定时间范围内

        Args:
            start (str, optional): 起始时间. Defaults to "00:00".
            end (str, optional): 终止时间. Defaults to "09:00".

        Returns:
            bool: 结果
        """
        now_date = str(datetime.now().date())
        start_time = datetime.strptime(now_date + start, '%Y-%m-%d%H:%M')
        end_time = datetime.strptime(now_date + end, '%Y-%m-%d%H:%M')
        now_time = datetime.now()
        if all([now_time > start_time, now_time < end_time]):
            return True
        else:
            return False

    @staticmethod
    def time_stamp_to_time(time_stamp: str, unit="s" or "ms", fmt="%Y-%m-%d %H:%M:%S") -> str:
        """时间戳转时间

        Args:
            time_stamp (str): 时间戳
            unit (str, optional): 单位. Defaults to "s"or"ms".
            fmt (str, optional): 日期时间格式. Defaults to "%Y-%m-%d %H:%M:%S".

        Raises:
            ValueError: 单位输入错误异常

        Returns:
            str : 转换的日期时间
        """

        if unit == "ms":
            time_stamp = float(time_stamp) / 1000
        elif unit == "s":
            time_stamp = float(time_stamp)
        else:
            raise ValueError(
                "time_stamp's unit input error, unit value in ['s', 'ms']")
        t = datetime.fromtimestamp(time_stamp)
        return t.strftime(fmt)
