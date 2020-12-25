# -*- coding='utf8' -*-
#__author__='LiuJinYao'

"""
本文学习爬取小说内容：获取笔趣阁--牧龙师
观察小说网站：https://www.bqg34.com/article/115006/的html结构，其目录章节以ul.mulu_list下的a标签来显示和跳转各章节。
而在各具体章节里，如https://www.bqg34.com/article/115006/47100823.html的html结构中，其小说内容则在div#htmlContent中
最后，将获取出来的小说内容进行一些特殊字符的replace即可。
参考材料：https://www.cnblogs.com/BlackStorm/p/6359005.html  >> &nbsp的字符的replace
"""

import requests
from bs4 import BeautifulSoup

HOST= 'https://www.bqg34.com/'
PATH = '/article/115006/'

def getzhangjie(um=0):
    """
    获取章节
    :param um: 控制返回的目录章节的数量。默认全部
    :return: 返回章节列表 如[['第1章 这是个意外', '47100823.html'],[...],]
    """
    html = requests.get(HOST + PATH).text
    ul = BeautifulSoup(html,features='html.parser').find_all('ul',class_='mulu_list')
    # 先获取ul的内容,然后在获取a标签的内容
    a = BeautifulSoup(str(ul[0]),features='html.parser').find_all('a')
    print(a)
    # 获取 a标签的string 和  'href'属性值
    zj = list(map(lambda x: [x.string,x.get('href')], a))
    print(f'获取章节成功，共有{len(zj)}章')
    return zj if um == 0 else zj[:um]

def content(list):
    """
    获取小说正文
    :param list: 章节信息。如['第1章 这是个意外', '47100823.html']
    :return:  章节+正文
    """
    text= requests.get(HOST+PATH+list[1]).text
    bf = BeautifulSoup(text,features='html.parser')
    contents = bf.find_all('div',id='htmlContent')
    # print(f'获取章节成功：{list[0]}')
    return list[0] + contents[0].text.replace('\xa0'*4,'\n\n')

def result(um=0):
    s = ''
    for i in map(content, getzhangjie(um)):
        s += '\n\n'+str(i)
    else:
        return s

if __name__ == '__main__':
    # getzhangjie()
    # print(content(['第1章 这是个意外', '47100823.html']))
    print(result(um=2))