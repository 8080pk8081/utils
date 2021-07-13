#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/26 15:27
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : app_run.py
from utils.app_utils import *

app = new_app()

if __name__ == "__main__":
    # os_exec('sh  ./bin/kill_sh.sh  celery ')
    # sleep(2)
    # os_exec('sh  ./bin/kill_sh.sh  flower ')
    # sleep(5)
    # os_exec('nohup  celery -A celery_tasks.tasks  worker --loglevel=INFO   --pool=solo  -E >> ./celery_tasks/celery.log  2>&1 &')
    # sleep(10)
    # os_exec('nohup  celery flower  --address=0.0.0.0 --port=5555   --broker=redis://localhost:6379/0  --auto_refresh=True  --persistent=True   >> ./celery_tasks/flower.log  2>&1 &')
    kwargs = {"host": '0.0.0.0', "port": 8282, "debug": True}
    app.run(**kwargs)
