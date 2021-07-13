#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/26 15:38
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : setting.py
""" 本文存放基础配置项 """

import os
from logging.config import dictConfig


from applications.app1 import env

# 蓝图列表
BP = [env]


# mysql信息配置
HOST = '10.119.92.35'
PORT = '3306'
DATABASE = 'sdwan'
USERNAME = 'root'
PASSWORD = '123456'

# APP实例配置
config_dict = {
    'SQLALCHEMY_DATABASE_URI': f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8",
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_COMMIT_ON_TEARDOWN': True,
    'SQLALCHEMY_ECHO': False,
    'CELERY_BROKER_URL': 'redis://localhost:6379/0',
    'CELERY_RESULT_BACKEND': 'redis://localhost:6379/0'
}

# celery实例配置
celery_dict = {
    'CELERY_TIMEZONE': 'Asia/Shanghai',
    'CELERY_TASK_RESULT_EXPIRES': 24 * 60 * 60 * 30,     # 任务结果最大时长
    'CELERYD_CONCURRENCY': 2,        # worker并发数
    'CELERYD_MAX_TASKS_PER_CHILD': 200,   # worker的生命周期为200个任务
    'CELERYD_TASK_TIME_LIMIT': 24 * 60 * 60 * 2
    # 'CELERY_TASK_SERIALIZER': 'msgpack',   # 任务序列化
    # 'CELERY_RESULT_SERIALIZER': 'msgpack',  # 结果序列化
    # 'CELERY_ACCEPT_CONTENT': ['msgpack']   # 任务允许类型
}

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# 声明项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
