#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""
本文探讨三元表达式的三种写法
"""

# 第一种写法
b =4
a =0 if b>0 else b
print(a)

# 第二种写法  #{True:值,False:值}[表达式]

a={True:0,False:b}[b>0]
print(a)

# 第三种写法  #定义一个元组，（"FalseValue", "TrueValue"）[表达式]    ps:注意False的值在前。
a= (1,0)[b>0]
print(a)