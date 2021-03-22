#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/9 19:23
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 多线程_线程池_ThreadPoolExecutor.py
"""
本文利用concurrent.futures模块实现线程池（线程池执行器）
参考材料：
https://www.cnblogs.com/zhang293/p/7954353.html
http://c.biancheng.net/view/2627.html
https://www.jianshu.com/p/6d6e4f745c27

ThreadPoolExecutor：线程池实例  max_workers=3 最大并发数
submit() 将任务加入到线程池 返回该任务的句柄。Future对象。
done()   任务是否结束，ture  false
result()  阻塞主线程，该线程任务完成了，才会解除主线程的被阻塞状态
with   线程池实现了上下文管理协议，所以可以用with语句来管理线程池，避免手动关闭线程池。
add_done_callback()  任务的回调函数，入参为需要调用的函数。可以通过此回调函数获取结果，这种方法，不会阻塞主线程。当线程任务完成后，程序会自动触发该回调函数，并将对应的 Future 对象作为参数传给该回调函数。
map()  阻塞主线程。线程池的map方法，跟全局函数的map()方法差不多。区别只是在于线程池的map方法是为iterables元素启动线程来执行，以并发的方式来执行func函数。最终收集每个线程的执行结果。 阻塞主线程。
wait()  阻塞主线程，直到满足设定的要求
cancel() 取消排队中的任务。即max_workers外的，未开始处理的任务可以被取消。
as_completed()函数。当某个任务结束了，就给主线程返回结果。  as_completed() 方法是一个生成器，在没有任务完成的时候，会一直阻塞，除非设置了 timeout。当有某个任务完成的时候，会 yield 这个任务，就能执行 for 循环下面的语句，然后继续阻塞住，循环到所有的任务结束。同时，先完成的任务会先返回给主线程。
"""
import random
import time
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def pro_case(count,tags):
    """
    逻辑函数，业务函数
    @param count: 循环次数
    @param tags: 任务标识符
    @return:
    """
    print('任务标识：',tags)
    for j in range(count):
        data = random.randint(1,99)
        sleep(random.randint(1,30))
        print(f'{data} is done')
    else:
        return f'任务标识-{tags} is done. result is ture!'

def case1():
    """
    手动加入、关闭线程池；阻塞主线程等待线程结果 result()
    """
    # 引用线程池执行器，创建最大线程数为3个的执行器实例
    pool = ThreadPoolExecutor(max_workers=3)
    # 往线程池加入一个任务
    task1 = pool.submit(pro_case,2,'1')
    task2 = pool.submit(pro_case,3,'2')
    task3 = pool.submit(pro_case,1,'3')
    task4 = pool.submit(pro_case,3,'3')
    # 判断future1代表的任务是否结束
    print('task1 done?',task1.done())
    time.sleep(3)
    # 判断future2代表的任务是否结束
    print('task2 done?',task2.done())
    # 查看future1代表的任务返回的结果  调用result来获取线程任务的返回值，但该方法会阻塞进程往前主线程，只有等线程任务完成后，result()方法的阻塞才会被解除
    print(task1.result())
    print('rensult1方法阻塞我了。所以现在才出来')
    # 查看future2代表的任务返回的结果
    print(task2.result())
    print('rensult2方法阻塞我了。。所以现在才出来')
    # 关闭线程池 记得关闭线程池
    pool.shutdown()
    print('task1 done?',task1.done())
    time.sleep(3)
    # 判断future2代表的任务是否结束
    print('task2 done?',task2.done())
    # 查看future1代表的任务返回的结果
    print(task1.result())
    print('rensult1方法阻塞我了。。所以现在才出来')
    # 查看future2代表的任务返回的结果
    print(task2.result())
    print('rensult2方法阻塞我了。。所以现在才出来')


def case2():
    """
    自动管理线程池，以回调函数的方法获取线程结果。不阻塞主线程。 *****
    """
    with ThreadPoolExecutor(max_workers=2) as pool:
        task1 = pool.submit(pro_case, 2, '1')
        task2 = pool.submit(pro_case, 3, '2')
        task3 = pool.submit(pro_case, 1, '3')
        task4 = pool.submit(pro_case, 3, '4')
        sleep(2)
        print('取消任务4，result is',task4.cancel())
        def get_result(task):
            print('任务结果是：',task.result())
        task1.add_done_callback(get_result)
        task2.add_done_callback(get_result)
        task3.add_done_callback(get_result)
        # task4.add_done_callback(get_result)
        print('我并未被阻塞--------')


def case3():
    """
    自动管理线程池，使用线程池的map方法，自动加入线程池任务及执行，收集结果。但阻塞主线程。
    """
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = pool.map(pro_case,(2, 3, 1, 3), ('1', '2', '3', '4'))
        print('--------------')
        print('results is :',results)
        for r in results:
            print(r)
        print("map函数获取结果也是阻塞主线程的。好了，任务执行完了，主线程被解除阻塞状态")

def case4():
    """
    批量增加线程池任务，使用wait方法，自定义停止等待，恢复主线程的条件。或timeout 或FIRST_COMPLETED 或ALL_COMPLETED。一般可用于后续代码依赖某个线程结果的情况。
    """
    from concurrent.futures import wait,FIRST_COMPLETED,ALL_COMPLETED
    with ThreadPoolExecutor(max_workers=2) as pool:
        data = [(2, '1'), (3, '2'), (1, '3'), (3, '3')]
        all_tasks = [pool.submit(pro_case, d[0], d[1]) for d in data]
        print(all_tasks)# 任务句柄 >> [<Future at 0x34af330 state=running>, <Future at 0x3513bb0 state=running>, <Future at 0x35139d0 state=pending>, <Future at 0x3513a90 state=pending>]
        wait(all_tasks,return_when=FIRST_COMPLETED)   # 等到第一个任务结束则返回。
        print('finished')
        print(wait(all_tasks, timeout=1.5))   # 超时返回。但不会影响任务及线程池本身。查看各任务状态。# >>  DoneAndNotDoneFutures(done={<Future at 0x34af330 state=finished returned str>}, not_done={<Future at 0x3513a90 state=pending>, <Future at 0x3513bb0 state=running>, <Future at 0x35139d0 state=running>})
        print('timeout, but still running ')

def case5():
    """
    as_completed()函数。当某个任务结束了，就给主线程返回结果。  as_completed() 方法是一个生成器，在没有任务完成的时候，会一直阻塞，除非设置了 timeout。当有某个任务完成的时候，会 yield 这个任务，就能执行 for 循环下面的语句，然后继续阻塞住，循环到所有的任务结束。同时，先完成的任务会先返回给主线程。
    @return:
    """
    from concurrent.futures import as_completed
    with ThreadPoolExecutor(max_workers=4) as pool:
        data = [(2, '1'), (3, '2'), (1, '3'), (3, '3')]
        all_tasks = [pool.submit(pro_case, d[0], d[1]) for d in data]
        for future_obj in as_completed(all_tasks):
            result = future_obj.result()
            print(f"main:{result}")


if __name__ == '__main__':
    # case1()
    # case2()
    # case3()
    # case4()
    case5()