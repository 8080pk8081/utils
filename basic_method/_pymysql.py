#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm
import _pymysql

class pymysql_action():
    def mysql_connect(self):
        en = input("请输入环境：\n1:测试环境\n2:预发布环境")
        if en =="1":
            ID = "测试环境"
        elif  en =="2":
            ID = "预发布环境"
        database = input("你想操作哪个模块的数据库")
        if "车" in database:
            host ="车辆"
            print("已经连接"+host+"打印所有的sql")
            action = input("请输入想要干的操作")
            if "信息" in action:
                plateno = input("请输入车牌号")
                print("车辆%s信息如下"%plateno)
            if  "实时" in action:
                plateno = input("请输入车牌号")
                print("车辆%s实时信息如下"%plateno)

if __name__ == '__main__':
    pymysql_action().mysql_connect()