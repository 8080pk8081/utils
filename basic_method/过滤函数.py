#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""
本文探索filter函数的使用
filter函数是将一个可迭代的数据进行函数处理，将处理结果与入参本身挂钩;然后会将处理结果为False（或等同于False）的入参丢弃，最后返回处理结果为Ture的入参集(filter对象)。
"""
def filterdata(x):
    return True if x > 1 else False   # 如果入参数大于1，给他一个True结果（1，‘23’，[1]等都行）；否则给他一个False结果（0,‘’,[]等都行）



if __name__ == '__main__':
    data=[0,4,2,5,6,7,-1,-2]
    a = filter(filterdata,data)   #>> a python3的filter函数，返回一个可迭代的对象
    print(a)   # <filter object at 0x03017690>
    print(list(a))   # [4, 2, 5, 6, 7]
    print(list(filter(lambda x: x > 5, data)))  # 与lambda函数组合使用




