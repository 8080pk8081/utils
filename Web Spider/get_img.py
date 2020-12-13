# -*- coding='utf8' -*-
#__author__='LiuJinYao'

"""
本文学习爬取图片：
目标在ul.pli中
"""
import requests
from bs4 import BeautifulSoup



def getsrc(search,um:int):
    """

    :param search: 需要搜索的内容 如 美女
    :param um:   查询几页内容 ，如 2
    :return:   图片链接集
    """
    result = []
    for i in range(um):
        url = f'https://www.ivsky.com/search.php?q={search}&PageNo={i+1}'
        text = requests.get(url).text
        bf = BeautifulSoup(text,features='html.parser')
        content = bf.find_all('ul',class_='pli')
        rc = BeautifulSoup(str(content),features='html.parser').find_all('img')
        result.append(list(map(lambda x : x.get("src"),rc)))
    return result



if __name__ == '__main__':
    print(getsrc('美女',2))
