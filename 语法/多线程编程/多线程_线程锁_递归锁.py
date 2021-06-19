#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/22 17:03
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程_线程锁_递归锁.py
"""
本文探索多线程--线程锁的使用。
递归锁：threading.RLock()
"""
import threading

num, num2 = 0, 0
lock = threading.RLock() #递归锁
# 多个锁。RLock
def run1():

    print("start run1...")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num
def run2():
    print("start run2...")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2
def run3():
    lock.acquire()
    res = run1()
    print('run1 done. start run2...')
    res2 = run2()
    lock.release()
    print('run2 done. result is ',res, res2)

for i in range(3):
    t = threading.Thread(target=run3)
    t.start()
while threading.active_count() != 1:
    print('有效线程数：',threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)
