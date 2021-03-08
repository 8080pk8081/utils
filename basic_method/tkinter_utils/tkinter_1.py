#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/31 4:11 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : tkinter_1.py
"""本文探索GUI程序的开发及使用"""

from tkinter import *
tk = Tk()
tk.title("我的第一个GUI程序")
tk.geometry("240x240")
lb = Label(tk,text='标签1')
lb.pack()
tk.mainloop()
