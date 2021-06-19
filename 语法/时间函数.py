#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/27 3:59 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 时间函数.py


import time

#默认秒级数据
now = time.time()
print(now)
#10位时间戳
r= int(now)
print(r)
#13位时间戳
rr = int(round(now*1000))
print(rr)
#时间
rrr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now))
print(rrr)
