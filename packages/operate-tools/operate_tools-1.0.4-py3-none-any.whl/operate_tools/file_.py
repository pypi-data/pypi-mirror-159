#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   file_.py
@Time    :   2022/07/20 15:48:19
@Author  :   Desire
@Version :   1.0
@Desc    :   文件操作
"""

import os
import sys

sys.path.insert(1, os.getcwd())
# here put the import lib

__all__ = ["FileTools"]

from chardet import UniversalDetector


class FileTools(object):

    @staticmethod
    def get_encode(file: str) -> str:
        """获取文件的编码格式

        Args:
            file (str): 文件路径

        Returns:
            str: 编码格式
        """
        with open(file, 'rb') as f:
            detector = UniversalDetector()
            for line in f.readlines():
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            return detector.result['encoding']

    @staticmethod
    def convert_encode(file: str, encode="utf-8") -> dict:
        """编码格式转换

        Args:
            file (str): 物件路径
            encode (str, optional): 要转换的编码格式. Defaults to "utf-8".

        Returns:
            dict: 转换结果
        """
        original_encode = FileTools.get_encode(file)
        if original_encode == encode:
            with open(file, 'rb') as f:
                file_content = f.read()
            file_decode = file_content.decode(original_encode, 'ignore')
            file_encode = file_decode.encode(encode)
            with open(file, 'wb') as f:
                f.write(file_encode)
        return {"file": file, "original_encode": original_encode, "now_encode": encode}
