#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao


str = """
from time import sleep
def load():
    sleep(1)
    return 1
if __name__ == '__main__':
    print(load())
"""
exec (str)

