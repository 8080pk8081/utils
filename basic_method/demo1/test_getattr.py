# from appium.webdriver.webdriver import WebDriver
# from selenium import webdriver
#
#
# class  def_1():
#     pass
#     """定位及其他方法"""
#     # def __init__(self):
#     #     self.driver = webdriver.Chrome()
#
# # class action1():
# #     """映射key和方法"""
# #     def __init__(self):
# #         def_2 = def_1()
# #         self.input1 = def_2.input1("loc",'2')
# #         self.info1 =  def_2.info1('haha')
#
#

case1 = ['input1', 'info1', 'gg']
class  Test_Case:
    def input1(self,msg):
        print("y")
    def info1(self,msg):
        print(msg)
    def test_case_action(self):
        if isinstance(case1, list):
            for case in case1:
                if hasattr(Test_Case(),case):
                    getattr(Test_Case(),case)(msg='lalaa')

                else:
                    print('keyword:{case}不在代码内'.format(case=case))
        else:
            print("yaml文件格式有误")
if __name__ == '__main__':
    GG = Test_Case()
    GG.test_case_action()


# import yaml
# class  Test_yamll:
#     def test_yamm(self):
#         yaml1=yaml.safe_load(open('GG.yaml', 'r', encoding='utf8'))
#         for dict in yaml1 :
#             # print(dict.keys())
#             for i in dict.keys():
#                 print(i)
#                 print(dict[i])
#
# if __name__ == '__main__':
#     Test_yamll().test_yamm()