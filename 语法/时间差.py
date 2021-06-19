#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao""
import datetime

def date_subtraction(s,e):
    """
    两个日期相减：如2020-11-27 12:07:41  -  2020-11-25 12:07:21   =2
    :param s: 开始时间
    :param e: 结束时间
    :return: 结束时间-开始时间， 整天数。
    """
    startTime = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    endTime = datetime.datetime.strptime(e, "%Y-%m-%d %H:%M:%S")
    day = (endTime - startTime).days
    return str(day)

if __name__ == '__main__':
    a= date_subtraction('2020-11-25 12:07:21', '2020-11-27 12:07:41')
    print(a)
    print(type(a))