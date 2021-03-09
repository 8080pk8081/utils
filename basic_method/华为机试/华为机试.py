#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/28 6:17 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试.py

# string = """The Furthest distance in the world, Is not between life and death, But when I stand in front of you, Yet you don't know that I love you."""
# str2 = "don't"
#
# data_list = string.split(" ")
# data_content = sorted(data_list)
# result = []
# str2 = str2.split("'")
# for str2 in str2:
#     for i in data_content:
#         if i.startswith(str2):
#             if i.isalpha() or i[-1].isalpha():
#                 result.append(i)
#             else:
#                 result.append(i[:-1])
# else:
#     result = set(result)
#     if result:
#         for j in result:
#                 print(j)
#     else:
#         print(str2)


i = ['5','10 5 0 1 3 2','30']
max_jie = i[0]
jie =[i for i in range(int(i[0])+1)]
count = i[1].split(" ")
user_need = int(i[-1])
# 信道容量
data = [2**i for i in range(int(i[0])+1)]
print(jie,data,count)
a = []
for i in zip(data,count):
    a.append(list(i))
print(a)
count = 0
while True:
    if int(a[-1][0]) >= user_need and int(a[-1][1]) > 0 :
        count += int(a[-1][1])
        a.pop(-1)
    elif user_need // int(a[-1][0]) < int(a[-1][1]):
        count += user_need // int(a[-1][0])
        le =int(a[-1][1]) - user_need // int(a[-1][0])
        if le == 0:
            a.pop(-1)
        else:
            a[-1][1] = le
    else:
        need = user_need - int(a[-1][0])*int(a[-1][1])
        for j in range(2):
            print(j)
            if int(a[j][0])*int(a[j][0]) >= need:
                count +=1
                break
        else:
            break
print(count)

#
#
#
#
#
