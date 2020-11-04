"""str_replace (替换）"""
"""将str的值中的字母替换"""

"""
输入一堆数据
1.非数字类型的字符索引
2.有几段数字
"""
str11 = input(">>>>>").strip()
a = 0
for i in str11:
    if i.isalpha():         #判断字符是不是字母
        str11 = str11.replace(i," ")    #   是的话就替换成空值
        print(a)
    a = a +1
print(str11)
list1 = str11.split()
print(list1)
print(len(list1))