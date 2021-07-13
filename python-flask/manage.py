#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/26 18:42
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : manage.py
"""
本文实现flask-migrate进行数据库迁移管理操作，注意因本项目对module的定义，是 module与app实例分离的，所以除了要modules要导入外，实例的db也是要导入的。
python manage.py  manager init   // 初始化生成migrations文件夹及env环境配置
python manage.py   manager  migrate  // 生成脚本
python manage.py  manager  upgrade   //  同步脚本
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app_run import app, db
from modules.module import *


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command(MigrateCommand)


if __name__ == '__main__':
    manager.run()