#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

def filterdata(x):
    return None if x>1 else x

if __name__ == '__main__':
    data=[0,4,2,5,6,7,-1,-2]
    a = filter(filterdata,data)   #>> a python3的filter函数，返回一个可迭代的对象
    print(a)
    print(list(a))




