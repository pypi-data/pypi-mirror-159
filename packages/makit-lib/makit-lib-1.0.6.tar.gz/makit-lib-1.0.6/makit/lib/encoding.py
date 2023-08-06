#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: LiangChao
@email：liang20201101@163.com
@desc: 
"""


def convert_bytes(s, encoding='utf-8', errors='strict'):
    if isinstance(s, bytes):
        return s
    elif isinstance(s, memoryview):
        return bytes(s)
    return str(s).encode(encoding, errors)
