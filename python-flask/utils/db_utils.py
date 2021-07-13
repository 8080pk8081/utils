#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/26 15:53
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : db_utils.py
"""
    本文实现flask—中间件 相关通用方法 主要是单独提取出来 分离model和app的关系，避免循环引用问题。
    参考材料：https://blog.csdn.net/ithongchou/article/details/103905800
"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()