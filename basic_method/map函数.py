#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

def fun1(x):
    return x ** 2


def fun2(x, y):
    return x ** 2 + y


def fun3(x, y):
    print(x ** 2 + y)


if __name__ == '__main__':
    result1 = map(fun1, [1, -1, 3, 5, 6])
    print(result1)  # <map object at 0x02FB7790>
    print(list(result1))  # [1, 1, 9, 25, 36]
    result = map(fun2, [1, -1, 3, 5, 6], [4, 4, 4, 4, 5])
    print(result)  # <map object at 0x02FC17D0>
    print(list(result))  # [5, 5, 13, 29, 41]
    result = map(fun3, [1, -1, 3, 5, 6], [4, 4, 4, 4, 5])
    print(result)
    print(list(result))  # [None, None, None, None, None]
    print(list(map(lambda x: x+5,[1,4,7.5,4])))  # 与lambda函数组合使用   [6, 9, 12.5, 9]



