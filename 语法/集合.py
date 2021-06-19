#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm


"""集合的使用"""
set1 = {1,4,5,7,8}
set2 = {2,4,7,6,9}
set3 = set1 & set2   #交集
print(set3)
print(set1 | set2)    #并集
print(set1.union(set2)) #并集
print(set1 ^ set2)  #反交集
print(set1 - set2)  #差集 （set1独有的）
print(set1.difference(set2))#差集 （set1独有的）

print( set1 < set2)  #子集
print(set2  > set1)  #超集

#列表去重
li = [1,2,33,2,33,5,6,2,33]
set4 = set(li)   #转为集合，自动去重
print(set4)
li = list(set4)  #然后再将集合转为列表
print(li)
