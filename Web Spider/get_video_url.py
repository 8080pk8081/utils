# -*- coding='utf8' -*-
#__author__='LiuJinYao'

"""
本文学习爬取图片：
目录在ul#content中
"""
from time import sleep

import requests
from bs4 import BeautifulSoup
HOST = 'https://www.1bbc5fb269ed1d51.com'
URl1="HOST + f'/mlvideolist.x?tagid=7&page={page+1}'"    #自拍
URL2 = "HOST + f'/mlvideolist.x?tagid=3&page={page+1}'"  #国产
URL3 = "HOST + f'/mlvideolist.x?tagid=1&page={page+1}'"  #群交


def gethref(um:int,url):
    """
    :param um:   查询几页内容 ，如 2
    :return:   图片链接集
    """
    result = []
    for page in range(um):
        url = eval(url)
        text = requests.get(url,timeout=10).text
        bf = BeautifulSoup(text,features='html.parser')
        content = bf.find_all('ul',id='content')
        rc = BeautifulSoup(str(content),features='html.parser').find_all('a')
        result.append(list(map(lambda x : x.get("href"),rc)))
    return set(result[0])

def getdownloadurl(href):
    url = HOST+href
    try:
        text = requests.get(url,timeout=10).text
        content = BeautifulSoup(text, features='html.parser').find_all('div', class_='downurl')
        content = BeautifulSoup(str(content), features='html.parser').find_all('a')
        cc = list(map(lambda x: x.string, content))[0]
        print(cc)
        return cc
    except Exception as e:
        print(e)


def main(um,url):
    list = gethref(um,url)
    print(list)
    with open("downloadurl.txt", 'r+') as fo:
        for h in list:
            sleep(2)
            download = getdownloadurl(h)
            fo.seek(0, 2)
            fo.write('\n'+str(download))
        else:
            fo.close()
if __name__ == '__main__':
    # print(gethref(1,URl1))
    # print(getdownloadurl('/play.x?stype=mlvideo&movieid=19197'))
    re = main(1,URL2)