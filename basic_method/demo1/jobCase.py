import  allure
@allure.feature('定义功能3')
class case():
    def  add(self,a,b):
        print(a+b)
        return  a+b
if __name__ == '__main__':
    case().add()