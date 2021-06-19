#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/22 12:10
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程_线程锁_同步锁.py
"""
本文探索多线程--线程锁的使用。
互斥锁（同步锁）：threading.Lock()
递归锁：threading.RLock()
"""

import threading
a = 0
lock = threading.Lock()

def incr_lock(n):
    global a
    for j in range(n):
        lock.acquire()    # 上锁的方法
        a += 1
        print('incr after is ',a)
        lock.release()    # 解锁
        # 要注意的是上锁解锁之间是修改操作的代码

def decr_lock(n):
    global a
    for j in range(n):
        with lock:       # 使用lock则自动解锁。
            a -= 1
            print('decr after is ',a)

def case1():
    """
    同步互斥锁。Lock
    """
    # >> 不落锁的时候，可能出现负值。
    t_incr = threading.Thread(target=incr_lock, args=(100000,))   # >> 不落锁的时候，可能出现-值。
    t_decr = threading.Thread(target=decr_lock, args=(100000,))
    t_incr.start()
    t_decr.start()
    t_incr.join()
    t_decr.join()
    print(a)





if __name__ == '__main__':
    case1()
