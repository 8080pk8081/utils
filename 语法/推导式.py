#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""列表推导式"""

#[1,2,3,4,5,6,7,8,9,10]
# 能整除二的数值+20
aa =[1,2,3,4,5,6,7,8,9,10]

a = [i+20 if i%2==0 else i for i in aa]
print(a)



"""字典推导式"""

bb=[{'k1':'v1','k2':'v2'},{'k1':'k2','k22':'v2'}]

b={k["k1"]:'0' if 'k2' not in k else k['k2'] for k in bb }




