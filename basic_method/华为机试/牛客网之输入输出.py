#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/28 1:00 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 牛客网之输入输出.py

"""
输入描述:
多个测试用例，每个测试用例一行。
每行通过,隔开，有n个字符，n＜100
输出描述:
对于每组用例输出一行排序后的字符串，用','隔开，无结尾空格
输入例子1:
a,c,bb
f,dddd
nowcoder
输出例子1:
a,bb,c
dddd,f
nowcoder
"""

import sys
for i in sys.stdin:
    data_list = i.strip("\n").split(",")
    new_list = sorted(data_list)
    print(','.join(new_list))
