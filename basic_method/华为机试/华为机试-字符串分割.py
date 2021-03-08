#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/28 11:42 上午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试-字符串分割.py

"""
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理
"""

#
data1 = 'uri'
data2 = 'batkqdhjnrwtsmzidswdnenqpsblsszldyttytrgenaizwehntqiaaufble'
#
import sys
result = []
for line in sys.stdin:
    a = line.split()
    result.append(list(a[0]))
for j in result:
        if len(j) > 8:
            r = len(j)//8
            for i in range(r):
                print(''.join(j[8*i:8*(i+1)]))
            left = len(j)%8
            if left:
                print(''.join(j[-left:])+"0"*(8-left))
        else:
            print(''.join(j) + "0" * (8 - len(j)))

