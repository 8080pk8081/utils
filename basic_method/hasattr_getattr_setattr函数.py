#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liujinyao"



# hasattr

class aa1():
    def aa(self,**kwargs):
        print('aa方法',kwargs["key1"],kwargs["key2"])
    str = '123'

print(dir(aa1))
print(hasattr(aa1, 'aa'))
print(hasattr(aa1, 'str'))
print(hasattr(aa1, 'c'))

a = getattr(aa1(),'str') if hasattr(aa1(),'str')  else None        # 查询该对象是否有 str 属性，有的话获取其值。
aa = getattr(aa1(),'bb') if hasattr(aa1(),'bb')  else None
c = getattr(aa1(),'bb',None)                                      #getattr函数的第三个入参则指向没找到时的默认返回值。
print(a)
print(aa)
print(c)
kwarg = {
    "key1":"1",
    "key2":"2"
}
b = getattr(aa1(),'aa',None)(**kwarg)    #getattr 获取函数时,找到了函数之后，用()来将其实例化。对于入参，可以使用不定长参数

# 有则覆盖，没有则增加
setattr(aa1,"str1","i m str1")
print(aa1().str1)
setattr(aa1,"str","i m str")
print(aa1().str)


# 组合使用

getattr(aa1(),"str2",setattr(aa1,"str2","i m str2"))
print(aa1.str2)