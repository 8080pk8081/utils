#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm
"""
本文探索字符串的使用方法
find()方法
replace()方法
strip()方法
split()方法
isalpha()方法      -- 判断是否全是字母
SS.isdigit()方法   -- 判断是否全是数字
SS.isalnum()方法   -- 判断是否全是字母或数字
SS.islower()方法   -- 判读是否全是小写
SS.isupper()方法   -- 判断是否全是大写
"""

# find()方法，找到字符后，返回第一个该字符所在的位置索引。如果没有找到则返回-1。
S = ' bavdBDFa '
print(S.find('a'))
print(S.find("g"))

# replace()方法，查找并替换，可以指定替换次数。如果没有找到则不替换。不改变原来的值。
s1 = S.replace("a", "A")
s2 = S.replace("a", "A", 1)
s3 = S.replace("Z",'z')
print(s1)
print(s2)
print(s3)
print(S)


s4 = S.strip(" ")
print(s4)
s5 = S.split("a")
print(s5)

SS = '123'
print(SS.isalpha())
print(SS.isdigit())
print(SS.isalnum())
print(SS.islower())
print(SS.isupper())
print("-"*20)
SS = 'aaa'
print(SS.isalpha())
print(SS.isdigit())
print(SS.isalnum())
print(SS.islower())
print(SS.isupper())