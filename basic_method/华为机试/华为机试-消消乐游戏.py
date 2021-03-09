#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 11:36 上午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试-消消乐游戏.py

"""【
消消乐游戏】
游戏规则：输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同，就可以消除。 在字符串上反复执行消除的动作，直到无法继续消除为止，此时游戏结束。 输出最终得到的字符串长度。
输入描述：
输入原始字符串 str ，只能包含大小写英文字母，字母的大小写敏感， str 长度不超过100。
输出描述：
输出游戏结束后，最终得到的字符串长度
备注：输入中包含 非大小写英文字母 时，均为异常输入，直接返回 0
输入：gg
输出：0
"""

def input_check(a):
    if isinstance(a, str) and len(a) <= 100 and a.isalpha():
        return 1
    else:
        print("请规范输入")
        return 0

def console_list(oldlist:list):
     for i in range(len(oldlist)-1):
         if oldlist[i] == oldlist[i+1]:
             data = {"new_list":[oldlist[j] for j in range(len(oldlist)) if (j not in [i, i+1])]
                 ,"again":True}
             break
     else:
         data = {"new_list": oldlist, "again": False}
     return data

def pro():
    a=input()
    if input_check(a):
        content_list = list(a)
        while True:
            result = console_list(content_list)
            if result["again"]:
                content_list = result['new_list']
            else:
                break
        print(len(result["new_list"]))


if __name__ == '__main__':
    pro()