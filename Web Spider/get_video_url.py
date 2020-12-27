# -*- coding='utf8' -*-
#__author__='LiuJinYao'

"""
本文学习爬取视频下载链接：
目录在ul#content中
"""
from time import sleep
import requests
from bs4 import BeautifulSoup

host = r'http://www.a8e0e744fa9b81a7.com'



def gethref(um:int,path):
    """
    :param um:   查询几页内容 ，如 2
    :return:   图片链接集
    """
    result = []
    for p in range(um):
        page = f'page={p+1}'
        url = host+path+page
        text = requests.get(url,timeout=10).text
        bf = BeautifulSoup(text,features='html.parser')
        content = bf.find_all('ul',id='content')
        rc = BeautifulSoup(str(content),features='html.parser').find_all('a')
        result.append(list(map(lambda x : x.get("href"),rc)))
    r1 = []
    for i in result:
        r1.append(set(i))
    return r1

def getdownloadurl(href):
    url = host+href
    try:
        text = requests.get(url,timeout=10).text
        content = BeautifulSoup(text, features='html.parser').find_all('div', class_='downurl')
        content = BeautifulSoup(str(content), features='html.parser').find_all('a')
        cc = list(map(lambda x: x.string, content))[0]
        print(cc)
        return cc
    except Exception as e:
        print(e)


def main(um,path):
    list = gethref(um,path)
    print(list)
    with open("downloadurl.txt", 'r+') as fo:
        for l in list:
            for h in l:
                sleep(2)
                download = getdownloadurl(h)
                if download is not  None:
                    fo.seek(0, 2)
                    fo.write('\n'+str(download))
        else:
            fo.close()
if __name__ == '__main__':
    PATH1 = "/mlvideolist.x?tagid=7&"  # 自拍
    PATH2 = "/mlvideolist.x?tagid=3&"  # 国产
    PATH3 = "/mlvideolist.x?tagid=1&"  # 群交
    PATH4 = "/mlvideolist.x?tagid=6&"  # 野外
    PATH5 = "/mlvideolist.x?tagid=8&"  # 萝莉
    PATH6 = "/mlmovielisthd.x?classid=7&" #无码高清
    PATH7 = "/mlmovielist.x?tagid=14&"    #巨乳
    PATH8 = "/mlvideolist.x?tagid=4&"  # 欧美日韩
    # print(gethref(3,PATH2))
    # print(getdownloadurl('/play.x?stype=mlvideo&movieid=19197'))
    re = main(3,PATH8)