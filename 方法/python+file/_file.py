#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm
# """
# 1.文件路径:./file/sex.txt
# 2.编码方式：utf-8  gbk...
# 3.操作方式：只读，只写，追加，读写，写读
# #以什么编码格式保持的文件就以什么编码格式打开
# """
# "只读：r  " \
# "只读：rb(readbytes)：非文字类的文件读取、上传、下载、储存"
# f = open('./file/sex.txt',mode='r',encoding='utf-8')
# content = f.read()   #bytes->str  read进行了类型转换
# print("f=" + content)
# f.close()
# f = open('./file/sex.txt',mode='rb')
# content = f.read()   #bytes->str  read进行了类型转换
# print(content)
# f.close()
#
# "只写：w  没有此文件就创建；有则对文件重写" \
# "只写：wb (writebytes)"
# d  = open('./file/sex.txt',mode='w',encoding='utf-8')
# d.write('gg')
# d.close()
#
# "追加： a"
# h = open('./file/sex.txt',mode='a',encoding='utf-8')
# h.write('hh')
# h.close()
#
# "读写： r+"
# "先读后写，：读完内容后写入，相当于追加"
# k = open('./file/sex.txt',mode='r+',encoding='utf-8')
# print("K=" + k.read())
# k.write('tt')
# print(k.read())
# k.close()
#
# "先写后读，相当于在最前边写，占位，写完，再读，被占位的内容就丢了"
# KK = open('./file/sex.txt',mode='r+',encoding='utf-8')
# KK.write("TT")
# print(KK.read())
# KK.close()
#
# "写读：w+：先写，重写了再读，没啥意义了"
# "追加读：a+：先追加写，光标到了最后，然后再读，没啥内容。" \
# "如果需要读取内容，需要配合移动光标来使用"
#
#
"光标调节，对读的作用，seek()以字节为单位定光标位置的"
# RR = open('./file/sex.txt','r+',encoding='utf-8')
# print("光标还在前面，开始读："+ RR.read())
# print("光标在最后面，读："+ RR.read())
# RR.seek(0)
# print("光标回到了前面，读："+ RR.read())

"""功能详解
read是按字符为单位读内容，读取数量，可以限制读取的内容
seek是以按字节为单位定光标，读取数量的 移动中文字内容的光标时，注意移动的数量应为字符数*3
tell是告诉你光标的位置
"""
# RD = open('./file/sex.txt',mode='r+',encoding='utf-8')
# # print("第一次光标位置", RD.tell())
# # RD.seek(6)
# # print("第三次光标位置", RD.tell())
# # content  = RD.read(3)   #读3个字符
# # print(content)
# # print("第三次光标位置", RD.tell())
# # RD.seek(RD.tell()-3)  #这里注意，中文文件，需要填字节数*3
# # content1 = RD.read(3)
# # print(content1)
#
# print(RD.readable()) #是否可读的 ->bool
# print(RD.seekable())  #是否可以移动光标的  ->bool
# # line = RD.readline()  #一行一行地读
# # print(line)
# # lines = RD.readlines() #每一行当成列表中的一个元素，
# # print(lines)
# RD.close()
'''
with open()
'''
# with open('./file/sex.txt','r+',encoding='utf-8') as obj,\
#      open('./file/sex.txt','r+',encoding='utf-8') as f1:
#     """可以同时打开同一个文件"""
#     print(obj.read())
#     print(f1.readline())

"""注册/登录功能"""
username  = input("请输入你要注册的用户名：")
password = input("请输入你要注册的密码：")
with open("../../语法/file/list_login.txt", mode="w", encoding='utf-8') as f2:
    f2.write("{username}\n{password}".format(username = username,password =password))
print("恭喜你注册成功")
print("开始登录!")
username = input("请输入你要登录的用户名：\n")

with open("../../语法/file/list_login.txt", mode="r+", encoding='utf-8') as f3:
    line  = f3.readline().strip('\n')   #第一行已读
    print(line,type(line))
    if username == line:
        password =input("请输入密码：\n")
        if password == f3.readline():   #读第二行
            print("登录成功")
        else:
            print("密码错误")
    else:
        print("输入正确的用户名")