#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/8 8:54 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : app.py

from  flask import  Flask
from flask_sqlalchemy import SQLAlchemy

from db import *

app = Flask(__name__)
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL
# 自动保存
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 创建db操作实例
fdb = SQLAlchemy(app)


@app.route('/')
def hello_word():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=8001,debug=True)