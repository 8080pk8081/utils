#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/24 8:58 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 华为机试-内存资源分配.py
"""
【内存资源分配】
有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源，用户会进行一系列内存申请，需要按需分配内存池中的资源，返回申请结果成功失败 列表。分配规则如下： 1、分配的内存要大于等于内存申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用。 2、需要按申请顺序分配，先申请的先分配。 3、有可用内存分配则申请结果为true，没有可用内存分配则返回false。 注：不考虑内存释放。
输入描述：
输入为两行字符串： 第一行为内存池资源列表，包含内存粒度数据信息，粒度数据间用逗号分割，一个粒度信息内部用冒号分割，冒号前为内存粒度大小，冒号后为数量。资源列表不 大于1024，每个粒度的数量不大于4096 第二行为申请列表，申请的内存大小间用逗号分隔。申请列表不大于100000 如： 64:2,128:1,32:4,1:128 50,36,64,128,127
输出描述：
输出为内存池分配结果。 如：true,true,true,false,false
示例1：
输入：
64:2,128:1,32:4,1:128
50,36,64,128,127
输出：
true,true,true,false,false
"""

def check():
    a = '64:2,128:1,32:4,1:128'
    b = '50,36,64,128,127'
    result1 = \
        list(map(lambda x,y: 1 if int(x) <= 1024 and int(y) <=4096 else 0, [i.split(":")[0] for i in a.split(",")],[i.split(":")[1] for i in a.split(",")]))
    result2 = list(map(lambda x: 1 if int(x) <= 100000 else 0, [i.split(":")[0] for i in b.split(",")]))
    if all(result1) and all(result2):
        return a.split(","),b.split(",")
    else:
        print("填写有误")

def pro():
    args = check()
    source = args[0]
    apply = args[1]
    source = {i.split(":")[0]:i.split(":")[1] for i in source}
    sort_keys = [k for k,v in source.items()]
    sort_keys = sorted(sort_keys,key=int)
    result = ''
    for a in apply:
        for j in sort_keys:
            if int(a) > int(j) or int(source[j]) <= 0 :
                pass
            else:
                result+="ture,"
                source[j]=int(source[j])-1
                break
        else:
            result+="false,"
    else:
        return result[:-1]



if __name__ == '__main__':
    '64:2,128:1,32:4,1:128'
    '50,36,64,128,127'
    print(pro())