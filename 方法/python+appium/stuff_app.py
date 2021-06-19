# from time import sleep
#
# from appium import webdriver
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android' # 系统
# desired_caps['deviceName'] = '3HX0217311002113' # 手机设备号；通过adb devices获得
# desired_caps['platformVersion'] = '9'  # 安卓版本号
# desired_caps['appPackage'] = 'com.ldygo.qhzc.stuff'  # 包名
# desired_caps['appActivity'] = 'com.ldygo.qhzc.staff.ui.splash.SplashActivity'  # 活动名（各个手机系统内可能不一样）
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# desired_caps['newCommandTimeout'] = 600  # appium超时session时间
# Wb = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
# sleep(10)
# # print(Wb.page_source)
# for i in range(4):
#     Wb.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
#     sleep(1)
# print(Wb.page_source)


print('哈'*299)
'哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈'
'哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈'
from  selenium import  webdriver
wd = webdriver.Chrome()
wd.get(r'https://www.baidu.com')
wd.find_element()