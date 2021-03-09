#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/25 14:15
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 列表的使用.py

"""
本文探索list的用法
"""
import  random
# #列表与列表拓展
# list = [1,2,3,5]
# list1 = ['2',5,73,6]
# print(list1)
# list1.extend(list)
# print(list1)


# 通过简单的对数据源的增删来实现，锁机制。
list2=["17607660940",'11100000014','123000000000']
i =random.randint(0,len(list2)-1)
print(i)
op = list2.pop(i)
print(op)
print(list2)
list2.append(op)
print(list2)