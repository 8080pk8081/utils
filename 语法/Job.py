# #
# import sys
# #
# # # _str = 'wo are loee /n cd ll'
# # # result = []
# # # for a in _str.split('/n'):
# # #     # print(a)
# # #     for b in a.split(' '):
# # #         if len(b)>2:  result.append(b)
# # # # print(list)
# # # print(result)
# #
# # def case1():
# #     return 1
# # def case2():
# #     return 2
# # def case3():
# #     return 3
# #
# # fun =[case3(),case2(),case1()]
# #
# #
# # it = iter(fun)
# # # print(next(it))
# # # print(next(it))
# # # print(next(it))
# #
# # while True:
# #     try:
# #         print(next(it))
# #     except:
# #         break
# #
"""生成器"""
def case4():
    for a in range(20):
        yield a
"""迭代器"""
fun4 = case4()
while True:
    try:
        print(next(fun4))
    except:
        break
#
#
# # print(sum(i+i for i in range(5)))
#
#
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()


def case5(*args):
    for i in args:
        print("不定长参数值= "+i)
case5('1','2','5')