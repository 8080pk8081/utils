#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""
本文探索eval()函数的用法
核心理念是:eval函数入参是字符串，那么eval函数的作用是，将字符串前后的引号，双引号，多引号去掉，然后分析表达式，如发现它是可运算,就会执行运算（执行计算，返回，脚本语义等）；没有意义则会报错。
"""

a = """1*2"""
print(eval(a))

b = '{"k1":"v1"}'
print(eval(b))

c = 2
d = 'c+2'
print(eval(d))

def add1(x):
    return x+3
print(eval('add1(2)'))
print(add1(2))

# eval的安全性问题，如果恶意输入可执行语言，就会被执行。
s = 'print("is it safe??")'
b = eval(s)


# python3 中的exec()函数 相比eval()函数，更全面，可以执行更复杂的代码。


ss= "for i in range(5): print(i) "
exec(ss)

# sss = "while True: print(1)"
# exec(sss)


file = 'exec_debug.text'
with open(file,'r') as f:
    exec(f.read())


str = """
from time import sleep
def load():
    sleep(1)
    return 1
if __name__ == '__main__':
    print(load())
"""
exec (str)
