#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"
"""本文探索lambda函数的使用
匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
说明：一定非要使用lambda函数；任何能够使用它们的地方，都可以定义一个单独的普通函数来进行替换。我将它们用在需要封装特殊的、非重用代码上，避免令我的代码充斥着大量单行函数。
"""

a = lambda x,y,z:x*2+y+z
print(a(5,6,7))

list1 = [1,4,5,6,8]

print(list(map(lambda x:x*2,list1)))

#匿名函数返回None
b = lambda x: print(x)
b(12)
print(b(12))   # >> print() 返回None