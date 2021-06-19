#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

"""本文探索python内置函数dir()的作用"""

# str的属性


print('str:',dir(str))

print('list:',dir(list))

print('tuple:',dir(tuple))

print('dict:',dir(dict))
print('set:',dir(set))


class a:
    def aa(self):
        pass
    def bb(self):
        pass
    def cc(self):
        pass
    def dd(self):
        pass
    def ee(self):
        pass
print("a",dir(a))
print(a().__dir__)
