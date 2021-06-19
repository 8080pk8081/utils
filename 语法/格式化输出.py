#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author:ljy
# @Software:Pycharm
class common_print():
    def printSomething(self):
        """换行输出"""
        print("床前明月光，\n疑是地上霜。"
              "\n举头望明月，\n低头思故乡。")
        """同行输出"""
        print('我',end='')
        print('是',end='')
        print('谁')
        """格式化输出:%s 和 format """
        print("今天是%s好%s子"%("个","日"))
        a=("我叫{}，今年{}，爱好{},叫我{}。").format('law',26,'something','law')
        print(a)
        b = ("我叫{0}，今年{1}，爱好{2},叫我{0}。").format('law',26,'something')
        print(b)
        c = ("我叫{name}，今年{age}，爱好{hobby},叫我{name}。").format(age=26,name='law',hobby='something')
        print(c)
        """输出颜色标注字体"""
        print('\033[0;31m红色字体无高亮\033[0m')
        print("\033[1;31m红色字体有高亮！\033[0m")

if __name__ == '__main__':
    common_print().printSomething()