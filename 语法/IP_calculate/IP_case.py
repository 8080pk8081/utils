#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/25 17:35
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : IP_case.py

import IPy


# ips = IPy.IP('192.168.1.0/24')
# print([i for i in ips])

print('192.168.1.121' in IPy.IP('192.168.1.0/24'))