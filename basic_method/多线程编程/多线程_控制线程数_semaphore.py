#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/9 14:34
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程_控制线程数_semaphore.py


"""
控制线程数： threading模块中 Semaphore 和 BoundedSemaphore 是用来管理线程数的
Semaphore 管理一个计数器，每调用一次 acquire() 方法，计数器就减一，每调用一次 release() 方法，计数器就加一。
计时器的值默认为 1 ，计数器的值不能小于 0，当计数器的值为 0 时，调用 acquire() 的线程就会等待，直到 release() 被调用。
因此，可以利用这个特性来控制线程数量

需求1：有一个长数据列表，需要处理这个列表，求其各元素的平方。
        如果这个长数据列表有100w个数据，那么如果遍历每个数据都创建一个线程的话，那就相当于需要创建100w个线程，在创建和销毁线程的过程会耗费不必要的资源。
        应当是将数据分块来操作，一个线程来处理若干的数据。如4核处理器，根据10-20/核的数据算的话，建议是开50条线程，那么每条线程应该处理的数据量是，100w/50 .
"""
import random
import threading
from time import sleep

def fun1(d_list):
    """
    业务处理逻辑
    @param d_list:  数据源
    @return:  业务处理结果
    """
    print(d_list)
    return [d**2 for d in d_list]

class thread_main_semaphore(threading.Thread):
    """
    继承线程类，直接复写线程任务。 使用Semaphore控制线程数
    """
    def __init__(self, i, semobj, data_list):
        """
        @param i: 用于查看循环次数，无其他实际意义
        @param semobj:  计数器实例，用以调用release方法
        @param data_list:  需要处理的业务数据
        """
        super().__init__()
        self.i = i
        self.semObj = semobj
        self.data = data_list

    def run(self):
        print("the thread is : " + str(self.i))
        sleep(random.randint(1,15))
        print('result is ',fun1(self.data))
        print(f"the thread {str(self.i)} is done")
        # 线程执行完了之后，计数器声明释放，从而通知下一个进程开始
        self.semObj.release()

def pro_marn_semaphore(datalist,seq:int,maxsem=5):
    """
    多线程（定义最大线程数）处理批量数据
    @param datalist: 需要处理的数据源
    @param seq: 处理的数据长度
    @param maxsem: 最大线程数
    """
    # 实例化计数器，最大5个
    sem = threading.Semaphore(maxsem)
    print(sem)
    j = 1   # 设置每条进程处理10个数
    for i in range(len(datalist)//int(seq)+1):      # 控制循环次数。数据长度除以进程处理数据数，取余再+1 次即可
        # 每调用一次，计数器减1；
        sem.acquire()
        t = thread_main_semaphore(i, sem, datalist[(j - 1) * int(seq):j * int(seq)])     # 进行逻辑处理，将每次取seq个。
        t.start()      # start 就是触发run方法
        j += 1


if __name__ == '__main__':
    datalist = [1, 4, 6, 7, 9, 4, 2, 6, 43, 76, 22, 33, 56, 43, 64, 32, 23, 34, 23, 43, 234, 23, 34, 234, 234, 45, 4,
                65, 76, 355, 35, 7, 67, 87, 342, 6, 76, 353, 54, 7, 1, 4]
    pro_marn_semaphore(datalist, 10)
