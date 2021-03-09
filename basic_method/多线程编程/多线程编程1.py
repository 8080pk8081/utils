#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/8 9:29 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程编程1.py

"""
本文实现多线程的基本使用
join方法，是保证多线程执行完毕后，后执行后续的代码，常用于后续操作依赖于线程执行结果的保证
"""

import random
import threading
from time import sleep


def pro_case(data):
    print(data)
    sleep(random.randint(1,30))
    print(f'{data} is done')

def pro_main(datalist):
    thlist = []
    for i in datalist:
        thlist.append(threading.Thread(target=pro_case, args=i))
    print(thlist)
    print('当前活跃线程数为', threading.active_count())

    for j in thlist:
        j.start()
        print('当前活跃线程数为', threading.active_count(),threading.get_ident())
    # join方法，是保证多线程执行完毕后，后执行后续的代码，常用于后续操作依赖于线程执行结果的保证
    for z in thlist:
        z.join()
    print(1)

if __name__ == '__main__':
    data = ['2','1','5','3','6','3','5']
    pro_main(data)
    print('122211')