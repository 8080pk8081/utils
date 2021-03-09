#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 5:21 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试-数据拼接.py

"""
【数组拼接】
现在有多组整数数组，需要将它们合并成一个新的数组。合并规则：从每个数组里按顺序取出固定长度的内容合并到新的数组中，取完的内容会删除掉，如果该行不足固定长度或者已经为空，则直接取出剩余部分的内容放到新的数组中，继续下一行。
输入描述：
第一行是每次读取的固定长度，0<长度<数目
第二行是整数数组的数目，0<数目<1000
第3-n行是需要合并的数组，不同的数组用回车换行分隔，数组内部用逗号分隔，最大不超过100个元素。
输出描述：
输出一个新的数组，用逗号分隔。
示例1：
输入：
3 2     》》操作两次，第一次取3个；第二次取两个
2,5,6,7,9,5,7
1,7,4,3,4
输出：
2,5,6,1,7,4,7,9,5,3,4,7
"""

def somethingtodo(count,data):

    string = data[:int(count)]
    new_list = data[int(count):]
    return string,new_list

def pro():
    c = '3 2 7\n2,5,6,7,9,5,7,67,8\n1,7,4,3,4,6,8,9,0'
    data_list = c.split("\n")
    c,data = data_list[0].split(" "),[i.split(",")for i in data_list[1:]]
    print(c,data)
    result = ''
    for j in c:
        for z in range(len(data)):
            string,newlist = somethingtodo(j,data[z])
            data[z] = newlist
            for i in string:
                result += i+','
    print(result[:-1])





if __name__ == '__main__':
    pro()