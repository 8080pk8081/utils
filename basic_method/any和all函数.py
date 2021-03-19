#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""本文探索any()和all()函数
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空字符，None、False 外都算 True。
即 all ture 为ture ; any ture 为 ture
需要注意 any函数可迭代对象为空 >>False   all函数可迭代对象为空 >>True
"""

result1 = (0,None,0,1)
result2 = (1,4,6,2)
print(any(result1))    # >>True
print(any(result2))    # >>True
print(any([]))         # >>False
print(all(result1))    # >>False
print(all(result2))    # >>True
print(all([]))         # 可迭代对象为空 >>True