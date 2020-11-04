#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""
本文探讨三元
"""

def assign():
    a=1 if True else 0           #条件为真时的结果(1) if 判段的条件(ture) else 条件为假时的结果(0)
    print(a)
    aa = {True:1,False:0}[a==1]   #{True:值,False:值}[表达式]
    print(aa)
    aaa=(0,1)[a==1]               #定义一个元组，（"FalseValue", "TrueValue"）[表达式]    ps:注意False的值在前。
    print(aaa)

def ab(x):
    if x>1:
        return True

def assign1(x):
    a = 1 if ab(x) else 0
    print(a)



if __name__ == '__main__':
    assign()
    assign1(0)