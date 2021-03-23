#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/23 17:56
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : ip_calculate.py
"""
本文进行路由表分析
如128.36.202.186/20的有效IP地址为：128.36.192.1 - 128.36.207.254
"""


def getbin(string):
    """
    base_utils:  数字型转二进制并填充至8位
    @param string: 需要转二进制的数字型。
    @return:
    """
    b = bin(int(string,10))[2:]
    return b if len(b) == 8 else '0'*(8-len(b))+b

def getint(bin):
    """
    base_utils:  二进制型转十进制
    @param bin: 需要转十进制的二进制数据
    @return:
    """
    return str(int(bin,2))

def ipToip_bin(ip):
    """
    将IP地址转为二进制
    @param ip:  IP地址
    @return: 该IP地址的二进制地址
    """
    return '.'.join([getbin(s) for s in ip.split('.')])

def ip_binToip(ip_bin):
    """
    将二进制IP地址转为十进制IP地址
    @param ip_bin:
    @return:
    """
    return '.'.join([getint(s) for s in ip_bin.split('.')])

if __name__ == '__main__':
    ip_bin  = ipToip_bin('128.36.202.186')
    ip = ip_binToip(ip_bin)
    print(ip_bin)
    print(ip)