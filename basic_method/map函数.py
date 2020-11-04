#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

def fun1(x):
    return x**2

def fun2(x,y):
    return x**2+y

if __name__ == '__main__':
    result1 = map(fun1,[1,-1,3,5,6])
    print(result1)
    print(list(result1))

    result = map(fun2,[1,-1,3,5,6],[4,4,4,4,5])
    print(result)
    print(list(result))
