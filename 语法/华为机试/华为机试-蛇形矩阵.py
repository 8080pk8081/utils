#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/28 1:34 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试-蛇形矩阵.py

"""
递归与循环
示例1
输入
复制
4
输出
复制
1 3 6 10      0+1  0+1+2  0+1+2+3  0+1+2+3+4
2 5 9         0+1+2-1  0+1+2+3-1  0+1+2+3+4-1
4 8           0+1+2+3-2  0+1+2+3+4-2
7             0+1+2+3+4-3
n**2
"""

def all_length(num:int):
    if num == 0:
        return 0
    else:
        return num + all_length(num - 1)

i_data = int(input())
# i_data = 4
for j in range(i_data):
    index = 0
    for z in range(i_data-j):
        print(all_length(j+z+1)-j,end=' ')
    print('')
