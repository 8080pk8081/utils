#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"

def a(*args):
    k = args[0]
    l = args[1]
    print(k+1)
    print(l+2)

def aa(**kwargs):
    print(kwargs["hearders"])



if __name__ == '__main__':
    a(1, 2, 4, 6)
    aa(g="123",hearders=1)