#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 4:28 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试-射击成绩.py
"""
【统计射击比赛成绩】
给定一个射击比赛成绩单，包含多个选手若干次射击的成绩分数，请对每个选手按其最高3个分数之和进行降序排名，输出降序排名后的选手 ID序列。条件如下：
1、一个选手可以有多个射击成绩的分数，且次序不固定。
2、如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手。
3、如果选手的成绩之和相等，则成绩之和相等的选手按照其ID降序排列。
输入描述：
输入第一行，一个整数N，表示该场比赛总共进行了N次射击，产生N个成绩分数（2<=N<=100）。 输入第二行，一个长度为N整数序列，表示参与每次射击的选手ID（0<=ID<=99）。 输入第三行，一个长度为N整数序列，表示参与每次射击的选手对应的成绩（0<=成绩<=100）。
输出描述：
符合题设条件的降序排名后的选手ID序列。
示例1：
输入：
13
3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55
输出：
5,3,7,4
"""

def get_data():
    count = '13'
    p_list = ['3','3','7','4','4','4','4','7','7','3','5','5','5']
    core_list=['53','80','68','24','39','76','66','16','100','55','53','80','55']
    if len(core_list) == int(count):
        p = set(p_list)
        result = []
        for i in p:
            core = []
            for j in range(len(p_list)):
                if p_list[j] == i:
                    core.append(core_list[j])
            else:
                if len(core) >= 3:
                    core = sorted(core,key=int)[-3:]
                    core1 = [int(a) for a in core]
                    result.append({i:sum(core1)})
        return result
    else:
        print("error")

def get_seq():
    get_data()
    data = {}
    for i in get_data():
        data.update(i)
    result = sorted(data.items(), key=lambda d: d[1], reverse=True)
    for j in range(len(result)-1):
        # 冒泡排序
        if result[j][1] == result[j+1][1]:
            result[j],result[j+1] = result[j+1],result[j]
        else:
            pass
    else:
        r=''
        for z in result:
            r += str(z[0])+','
        else:
            print(r[:-1])


if __name__ == '__main__':
    get_seq()