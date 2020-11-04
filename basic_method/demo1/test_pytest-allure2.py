import allure
import pytest
from demo1.jobCase import case
a = 1
b = 2
@allure.feature('定义功能2')
class  Test_case():
    @allure.story("定义场景2")
    def test_case(self):
        with allure.step("定义步骤2"):
            C =case().add(a,b)
        with allure.step("断言2"):
            assert C == 7


if __name__ == '__main__':

    a=Test_case()
    a.test_case()