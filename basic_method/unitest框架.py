#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liujinyao"

from ddt import  ddt,data
import unittest

@ddt
class u1(unittest.TestCase):
    def setUp(self):
        print("setUp")
    @data(1,3,4,6,8)
    def test_case1(self,value):
        print(value)
    def test_case2(self):
        print("case2")
    def tearDown(self):
        print("tearDown")

class u2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.test_case1(cls)
    def test_case1(self):
        print("case1")
    def test_case2(self):
        print("case2")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()