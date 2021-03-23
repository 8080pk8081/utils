#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/23 8:34
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程实例_线程池_锁_队列.py

"""本文探索线程池、同步锁、队列的综合使用。
需求：有一个长度500的随机数列表。需要将他们的逐一求平方。
"""
import queue
import random
import threading
import time
from time import sleep

# 生成随机数
data = [str(random.randint(1,10000)) for j in range(50)]
print(data)
# 创建队列
qq = queue.Queue(maxsize=3)
# 创建同步锁
lock = threading.Lock()
result = []

def qq_put():
    # with lock:   # 这里上锁是为了保证取数的时候，一一从data里取，有顺序，如果不用顺序的话，则不用锁。
    while data:
        str = data.pop()
        qq.put(str)  # pop 方法取最后一个。
        print(threading.current_thread().name+f'推送了{str}')

def case_handler():
    while True:
        if qq.empty():   # 队列空了就退出。
            break
        else:
            num = int(qq.get(block=False))
            sleep(0.5)      # 加点等待时间，程序更稳定
            print(threading.current_thread().name+f'我取到的数字是{num}，它的平方值是{num**2}')
            result.insert(0,num**2)                 # 这里如果是需要逐个有顺序写入，也可以上同步锁。

def main_program():
    action = [threading.Thread(target=qq_put).start() for i in range(3)]
    action1 = [threading.Thread(target=case_handler) for i in range(3)]
    q = [t.start() for t in action1]
    q = [t.join() for t in action1]   # 这里应该我要把result打出来，所以就需要join线程。


if __name__ == '__main__':
    startTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    main_program()
    print(result)
    endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(startTime)
    print(endTime)