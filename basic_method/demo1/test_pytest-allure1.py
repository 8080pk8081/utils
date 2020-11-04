import allure

from jobCase import case
a = 1
b = 6
@allure.feature('定义功能1')
class  Test_case():
    @allure.story("定义场景1")
    def test_case(self):
        with allure.step("定义步骤1"):
            C =case().add(a,b)
        with allure.step("断言1"):
            assert C == 7

if __name__ == '__main__':

    a=Test_case()
    a.test_case()