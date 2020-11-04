#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm


class common_input():
    def inputSomething(self):
        """常规输入的使用"""
        username =input('请输入用户名:')
        password =input("请输入密码:")
        if username  =='law' and password == '123':
            result ='登录成功'
        else:
            result ='用户名或密码错误'
        return  result
    def input_Incount(self,count):
        '''输入限制'''
        case  = 0
        while case < count:
            result = self.inputSomething()
            print(result)
            if result =='登录成功':
               break
            case = case + 1
        if case >= count:
            print('登录次数达到上限')
    def input_strip(self):
        """对输入内容做优化，忽略空格等特殊字符"""
        username  = input('请输入用户名：').strip()
        print(username)
    def input_split(self):
        """对输入内容进行分割、拆分。输出为一个列表"""
        username  = input("请输入用户名：").split(',')
        print(username)
if __name__ == '__main__':
    common_input().input_split()

