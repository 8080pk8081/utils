#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/27 7:32 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 随机函数.py

import random
import string
# 随机整数
print(random.randint(1,100))
print(random.randrange(0,100,2))
# 随机字符--返回对象
print(random.choice(["1","23","dk","ij"]))
# 随机字符--返回列表对象
print(random.choices(["1","23","dk","ij"]))
# 固定长度的a-zA-Z0-9的字符组合
print(''.join(random.sample(string.ascii_letters+string.digits,5)))

