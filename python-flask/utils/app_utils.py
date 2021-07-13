#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/26 15:29
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : app_utils.py
""" 本文实现flask—app相关通用方法 """

# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask
from configs.setting import config_dict, project_path
from configs.setting import BP

from modules.module import db

def new_app():
    """
    new一个APP对象。 注册蓝图、应用上下文衔接。db链接实例等操作
    :return: APP对象
    """
    app = Flask(__name__, root_path=project_path)
    app.config.update(config_dict)
    register_blueprints(app, BP)            # 注册蓝图
    # 在modules与app分离的设计中，db = SQLAlchemy()  需要实例化 db 和 app_context() 实现应用上下文衔接  https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
    db.init_app(app)
    app.app_context().push()
    return app

def register_blueprints(app,bplist):
    """
    批量注册蓝图
    """
    [app.register_blueprint(obj) for obj in bplist]
    return None



