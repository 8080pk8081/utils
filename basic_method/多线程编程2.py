#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/8 9:29 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程编程2.py

""" 本文实现多线程的基本使用 """
import random
import threading
from time import sleep


def pro_case(data):
    sleep(random.randint(1,30))
    print(data)
    print(f'{data} is done')

def pro_main(datalist):
    thlist = []
    for i in datalist:
        thlist.append(threading.Thread(target=pro_case, args=i))
    print(thlist)

    for j in thlist:
        j.start()

    for z in thlist:
        z.join()

if __name__ == '__main__':
    data = ['2','1','5','3','6','3','5']
    pro_main(data)