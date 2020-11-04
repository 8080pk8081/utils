#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"
"""列表推导式"""
#[1,2,3,4,5,6,7,8,9,10]>>能整除2的数字加20>>一行写出来
aa =[1,2,3,4,5,6,7,8,9,10]
a = [i+20 if i%2 else i for i in aa ]
print(a)

b =[i+20  for i in aa if i%2 ]
print(b)


"""字典推导式"""
bb=[{'p':'p1','pd':'pd1'},{'p':'p2','pd':'pd2'}]      #>>{'p1': 'pd1', 'p2': 'pd2'}
print({k['p']:k['pd'] for k in bb})