#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   time_test.py
@Time    :   2022/07/13 17:05:14
@Author  :   Desire
@Version :   1.0
@Desc    :   None
"""

import os
import sys


sys.path.insert(1, os.getcwd())
# here put the import lib

from operate_tools.time_ import TimeTools


class TestTimeTools(object):

    def test_is_within_time_range(self):
        result = TimeTools.is_within_time_range()
        print(result)
        assert result == False
