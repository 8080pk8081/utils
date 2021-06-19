#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liujinyao"
import pytest

def fun_add(x:int):
    return x+1

def test_answer():
    assert  1 > 0
    return 1

def test_string():
    def aa():
        print('123')
    t = test_string()
    print(dir(t))
    assert  hasattr(t,'aa')

if __name__ == '__main__':
    pytest.main(['python+pytest.py'])