#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ljy
# @Software: PyCharm

casebase ={
        "菜单" : "新增菜单页面--",
        "菜单权限" :"新增的菜单受菜单和数据权限控制",
        "查询":"新增菜单的查询条件有：,可以单一查询和组合查询",
        "查询限制":"查询条件：，支持模糊搜索",
        "结果":"结果默认为空，展示的字段内容有：",
        "功能按钮":"新增的功能按钮有：受菜单权限控制",
        "结果展示" : "结果展示为15条/页。可正常上下翻页"
}
case = input("请输入新增菜单页面:")
basecase = "新增菜单页面--%s"%case
print(basecase)