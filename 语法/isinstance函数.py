#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""本文探索isinstance()函数"""

a = []
b = []
if isinstance(a,list):
    print("a is a list type")

if isinstance(a,(tuple,list,str)):
    print(" a is ok")

if type(a) ==list:
    print(1)


class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)
