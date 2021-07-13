#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/26 15:30
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : module.py
""" 本文为数据库表 ORM 模型表 """

from datetime import datetime
from utils.db_utils import db

# 升级包表
class package_info(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    package_name = db.Column(db.String(300), nullable=False,comment='升级包文件名')
    root_path = db.Column(db.String(350),nullable=False, comment='绝对路径')
    model = db.Column(db.String(10), comment='设备类型')
    version = db.Column(db.String(50), comment='升级包版本号')
    is_del =  db.Column(db.String(1), server_default='0', comment='0-未删除；1-已删除')
    package_info = db.Column(db.Text(16777216), comment='包info')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    def __repr__(self):
        """
        :return:
        """
        return f'<object_package_name is: {self.package_name}>'

# 宿主机表
class host_os(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    hostos_name = db.Column(db.String(300), nullable=False, comment='宿主机别名')
    host = db.Column(db.String(15), nullable=False, comment='宿主机IP')
    webusername = db.Column(db.String(15), comment='web用户名')
    webpwd = db.Column(db.String(50), comment='web密码')
    create_date = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    # to_json的写法是方便将查询结果json化显示。使用
    # reports = tasks_record.query.order_by(tasks_record.update_date.desc()).all()  # 倒序全量
    # reports = [x.to_json() for x in reports]
    def to_json(self):
        return {
                'id': self.id,
                'hostos_name': self.hostos_name,
                'host': self.host,
                'webusername': self.webusername,
                'webpwd': self.webpwd,
                'create_date': str(self.create_date),
                'update_date': str(self.update_date)
                }