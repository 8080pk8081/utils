#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/2 10:08
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : tasks.py
"""
本文实现异步任务相关的任务定义。
相关定义：
# task：任务
# broker（中间人）：存储任务的队列
# worker：真正执行任务的工作者
# backend：用来存储任务执行后的结果
相关命令：
ImportError: cannot import name 'Command'
celery -A celery_tasks.tasks  worker --loglevel=INFO   --pool=solo    # 注意这里的 -A 对应的项目为对应的py文件。
celery flower  --address=127.0.0.1 --port=5555   --broker=redis://localhost:6379/0

"""
from celery import Celery
from configs.setting import config_dict, celery_dict


celery = Celery('tasks', broker=config_dict['CELERY_BROKER_URL'], backend=config_dict['CELERY_RESULT_BACKEND'])
celery.config_from_object(celery_dict)


@celery.task
def task_upgrade_main(id):
    print(id)

if __name__ == '__main__':
    task_upgrade_main.delay(12)