#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/7 9:47
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : Kw_1.py


from robot.api.deco import keyword
class Kw_1:
    @keyword("关键字")
    def kw1(self):
       return  "123"

    @keyword("预期结果")
    def kw2(self,str1,str2):
        return "ture" if str(str1) == str(str2) else  "false"