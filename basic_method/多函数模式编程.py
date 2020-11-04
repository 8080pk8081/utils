#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"
"""
 本文探索多函数编程，认识面向对象的编程方式
  1.先定义一个方法1，要将属性值+1
  2.再定义一个方法2，要将属性值-3
  3.最后定义一个方法，将对象的属性进行方法1和方法2的处理。
"""

def f1(x):
    return x+1

def f2(x):
    return x-3

def ff(fun1,fun2,data):
    return fun1(data)+fun2(data)

if __name__ == '__main__':
    data =3
    result = ff(f1,f2,data)
    print(result)