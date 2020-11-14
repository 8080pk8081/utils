# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 8:46 下午
# @Author  : Liu Jin Yao
# @File    : 多线程编程.py
"""本文探索多线程编程"""

import  threading
from  time import sleep,ctime


def loop(nloop,s):
    """
    功能代码
    :param nloop:
    :param s:
    """
    print( "start loop",nloop,"at: ",ctime())
    sleep(s)
    print("loop",nloop,"done at: ",ctime())

def Main(loops):
    """
    多线程主流程：
        创建实例；
        开启进程；
        join进程；
    :param loops:
    :return:
    """
    print("beginning at:",ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        print("setUp",i,ctime())
        t = threading.Thread(target=loop,args=(i,loops[i]))     #进程1等待4s，进程2等待2s；
        threads.append(t)

    for i  in nloops:
        print("start",i,ctime())
        threads[i].start()

    for i in nloops:
        print("join",i,ctime())
        threads[i].join()

    print("done at:",ctime())
    return True

if __name__ == '__main__':
    loops = [50, 60]  # 等待时间
    a = Main(loops)
    if a:
        print("ok")
