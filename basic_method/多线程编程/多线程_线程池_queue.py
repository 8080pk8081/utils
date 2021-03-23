#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/22 12:06
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程_线程池_queue.py
"""
本文探索Queue队列实现线程通信
参考材料：
http://c.biancheng.net/view/2624.html
queue模块主要提供三个列。分别代表三种对列
1.queue.Queue(maxsize=0)：代表 FIFO（先进先出）的常规队列，maxsize 可以限制队列的大小。如果队列的大小达到队列的上限，就会加锁，再次加入元素时就会被阻塞，直到队列中的元素被消费。如果将 maxsize 设置为 0 或负数，则该队列的大小就是无限制的。
2.queue.LifoQueue(maxsize=0)：代表 LIFO（后进先出）的队列，与 Queue 的区别就是出队列的顺序不同。
3.PriorityQueue(maxsize=0)：代表优先级队列，优先级最小的元素先出队列。
这三个队列类的属性和方法基本相同， 它们都提供了如下属性和方法：
Queue.qsize()：返回队列的实际大小，也就是该队列中包含几个元素。
Queue.empty()：判断队列是否为空。
Queue.full()：判断队列是否已满。
Queue.put(item, block=True, timeout=None)：向队列中放入元素。如果队列己满，且 block 参数为 True（阻塞,默认），当前线程被阻塞，timeout 指定阻塞时间，如果将 timeout 设置为 None，则代表一直阻塞，直到该队列的元素被消费；如果队列己满，且 block 参数为 False（不阻塞），则直接引发 queue.FULL 异常。
Queue.put_nowait(item)：向队列中放入元素，不阻塞。相当于在上一个方法中将 block 参数设置为 False。
Queue.get(item, block=True, timeout=None)：从队列中取出元素（消费元素）。如果队列已满，且 block 参数为 True（阻塞），当前线程被阻塞，timeout 指定阻塞时间，如果将 timeout 设置为 None，则代表一直阻塞，直到有元素被放入队列中； 如果队列己空，且 block 参数为 False（不阻塞），则直接引发 queue.EMPTY 异常。
Queue.get_nowait(item)：从队列中取出元素，不阻塞。相当于在上一个方法中将 block 参数设置为 False。
"""

import queue
def queue_put():
    """
    put方法是加入任务。超过容量可能阻塞线程/报错queue.FULl；如果设置了超时时间，则等待一定时间后，还无法加入域任务则报错：queue.FULl
    """
    qq = queue.Queue(maxsize=2)   # 创建队列
    qq.put('123')  # 往队列里加元素
    qq.put('234')
    print('主线程未阻塞')
    print(qq.qsize())  #队列实际大小
    qq.put('555')   # 当队列的block参数为True且队列满了之后，再调用put方法，会阻塞线程
    print('线程阻塞了吗？')

def queue_get():
    """
    get方法是取出元素。先进先出。队列为空则阻塞/报错queue.EMPTY
    """
    qq = queue.Queue(maxsize=2)   # 创建队列
    qq.put('123')  # 往队列里加元素
    qq.put('234')
    arg1 = qq.get()   # 当队列的block参数为True且队列满了之后，再调用get方法，会阻塞线程
    print(arg1)
    arg2 = qq.get()
    print(arg2)
    print('主线程未阻塞')
    arg3 = qq.get()   # 当队列的block参数为True且队列空了之后，再调用get方法，会阻塞线程
    print(arg3)
    print('线程阻塞了吗？')

def case1():
    """
    批量加入对列
    """
    data = ['21','23','32','4','1',]
    q = queue.Queue(maxsize=0)
    result = [q.put(d) for d in data]
    print(result)
    print(q.qsize())

if __name__ == '__main__':
    # queue_put()
    # queue_get()
    case1()