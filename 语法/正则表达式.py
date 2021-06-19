# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 5:56 下午
# @Author  : Liu Jin Yao
# @File    : 正则表达式.py

import re


str = "['22','登陆成功'],['3','4'],['5','6']"

p="\['\w+','\w+'\]"     # \[ >> 以[开头   \] >>以]结束  '\w+' >>一个或多个字母数字字符，被''包裹  ,两个值之间还有一个英文逗号'
a = re.findall(p,str)
if a is not None:
    print(a)
