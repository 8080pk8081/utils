#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm
"""dict：  key 必须是不可变数据类型、可哈希 （元组、bool、int、str）
        valuse ：  任意数据类型
"""
dict  = {
    "name": "jy"
}
"""增"""
dict["age"]='27'   # 增，存在就覆盖
# dict["name"]='alex'  # 改
# dict.setdefault()    #没有就增加
# """删"""
# dict.pop("")   #按照key来删除，有返回值
# del dict['name']  #按照key来删除，没有返回值
# dict.popitem()   #随机删除，返回的是元组
# dict.clear()   #清空字典
# """改"""
# dict.update()
# """查"""
# dict.keys()     #所有的keys
# dict.values()   #所有的values
# dict.items()    #所有的键值对
# dict.get("name",None)   查询字典是否存在键
"""打印所有的键值对"""
for k, v in dict.items():
    print(k, v)
