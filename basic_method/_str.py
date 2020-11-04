#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm

class common_Str():
    def strSomething(self):
        s = "bbbadb"
        if s.find("c") > -1:   #find 的用法 。如果可以找到则返回该字段的索引，如果找不到则返回-1（int)
            print("字符存在")
        else:
            print("字符不存在")