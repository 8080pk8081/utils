import allure

from demo1.jobCase import case
a = 1
b = 9
@allure.feature('定义功能3')
class  Test_case():
    @allure.story("定义场景3")
    def test_case(self):
        with allure.step("定义步骤3"):
            C =case().add(a,b)
        with allure.step("断言3"):
            assert C == 7


if __name__ == '__main__':

    a=Test_case()
    a.test_case()


