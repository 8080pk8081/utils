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


def add_bin_spot(bin_not_spot_list):
    """
        给32位的二进制数，加3个点，分别是8位，17位，26位
    @param bin_not_spot_list: 32位二进制数的列表
    @return: string
    """
    action = [bin_not_spot_list.insert((i+1)*8+i,'.') for i in range(3)]
    return [''.join(bin_not_spot_list)][0]

def ip_to_ipBin(ip):
    """
    将IP地址转为二进制
    @param ip:  IP地址
    @return: 该IP地址的二进制地址
    """
    return '.'.join([getbin(s) for s in ip.split('.')])

def ipBin_to_ip(ip_bin):
    """
    将二进制IP地址转为十进制IP地址
    @param ip_bin:
    @return:
    """
    return '.'.join([getint(s) for s in ip_bin.split('.')])

# 1.计算子网掩码
def get_netMask(de_mask):
    """
    根据IP/掩码位 得出子网掩码二进制及子网掩码十进制
    @param de_mask: IP/掩码位数 如 128.36.202.186/20
    @return: (子网掩码二进制,子网掩码十进制)
    """
    mask = int(de_mask.split('/')[1])
    netMask = add_bin_spot(list(''.join(['1' for i in range(mask)])+'0'*(32-mask)))
    netMask_ip = ipBin_to_ip(netMask)

    return netMask, netMask_ip


def get_net_addr(de_mask):
    """
    根据IP/掩码位 计算网络地址
    @param de_mask: IP/掩码位数 如 128.36.202.186/20
    @return (网络地址二进制,网络地址十进制)
    """
    # 子网掩码二进制
    net_mask = get_netMask(de_mask)[0]
    # IP地址二进制
    ip_addr = ip_to_ipBin(de_mask.split('/')[0])
    net_addr = ''
    # 与运算
    for i in range(len(ip_addr)):
        if net_mask[i] == '1' and ip_addr[i] == '1':
            str = '1'
        elif net_mask[i] == '.':
            str = '.'
        else:
            str = '0'
        net_addr = net_addr + str
    else:
        return net_addr, ipBin_to_ip(net_addr)

def get_ip_validaddr(de_mask):
    mask = int(de_mask.split('/')[1])
    net_addr_bin,net_addr = get_net_addr(de_mask)
    # 网络地址
    print(net_addr)
    radio_net_addr_bin = list(net_addr_bin.replace('.',''))
    radio_net_addr_list = list(''.join(radio_net_addr_bin[:mask])+'1'*(32-mask))
    # 广播地址二进制
    radio_net_addr_bin = add_bin_spot(radio_net_addr_list)
    # 广播的地址十进制
    radio_net_addr = ipBin_to_ip(radio_net_addr_bin)
    print(radio_net_addr)


if __name__ == '__main__':
    data = '128.36.202.186/20'
    # ip_bin = ipToip_bin('128.36.202.186')
    # ip = ip_binToip(ip_bin)
    # print(ip_bin)
    # print(ip)
    print(get_ip_validaddr(data))