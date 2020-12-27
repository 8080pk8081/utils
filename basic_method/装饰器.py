#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""
本文档主要是研究python装饰器的原理及应用 -- docorator
    装饰器之闭包的概念
        1.函数嵌套 (函数内部定义函数)
        2.内部函数作为返回值返回
        3.内部函数必须要引用外部函数作用域里的变量。
    用途：
        1.logincheck
"""

x =4

def  log(fun):
    """
    带参数的普通装饰器
    :param fun:
    :return:
    """
    def warpper():             #1.函数嵌套(函数内部定义函数)
        text =11
        fun(text)                   #3.内部函数必须要引用外部函数作用域里的变量。
        print(3)
        print(x)                    # ps：x为全局变量，非外函数的局部变量
    return warpper                  #2.内部函数作为返回值返回

#装饰器带参数的
def logg(text):
    def warpper(fun):
        def inner_warpper(*args,**kwargs):
            print("前置")
            a = fun(text)
            print("后置")
            return  a
        return inner_warpper
    return warpper

@log
def pro(text):
    print(text)
    return text

@logg("nice")
def proo(t):
    print("中间")
    return t



if __name__ == '__main__':
    pro()
    print(proo())