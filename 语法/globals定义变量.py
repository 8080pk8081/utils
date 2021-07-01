#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/1 14:28
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : globals定义变量.py

# 定义全局变量
print(globals())
globals().update({'name': 1, 'age': 18})
print(name)
print(age)