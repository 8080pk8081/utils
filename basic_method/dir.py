
import os
import time
from datetime import datetime
from selenium import webdriver
import traceback

def createDir():
      '''生成当前日期字符串'''
      date = time.localtime()
      path = os.path.dirname(os.path.abspath(__file__))
      date_path = '-'.join([str(date.tm_year), str(date.tm_mon),str(date.tm_mday)])    #输出年-月-日
      # time_path = '-'.join([str(date.tm_hour), str(date.tm_min),str(date.tm_sec)])     #输出时-分-秒
      dateDir = os.path.join(path,date_path)     # 拼接路径
      #picturePath = os.path.join(savePath, pictureName+'.png')   #拼接路径
      # 如果当前日期目录不存的话就创建
      if not os.path.exists(dateDir):
            os.mkdir(dateDir)
      return dateDir    # 路径：D:\Python_work\test\2019-9-24




# def createDir():
#       '''创建当前日期和当前时间目录'''
#       path = os.path.dirname(os.path.abspath(__file__))
#       dateDir = os.path.join(path,currentDate())
#       # 如果当前日期目录不存的话就创建
#       if not os.path.exists(dateDir):
#             os.mkdir(dateDir)
#       # timeDir= os.path.join(dateDir,currentTime())
#       # #如果当前时间目录不存的话就创建
#       # if not os.path.exists(timeDir):
#       #       os.mkdir(timeDir)
#       return dateDir

# def takeScreenshot(driver,savePath,pictureName):
#     picturePath = os.path.join(savePath, pictureName+'.png')
#     try:
#         driver.get_screenshot_as_file(picturePath)
#     except Exception  as e:
#         print(traceback.print_exc())

if __name__ == '__main__':
    a = createDir()
    print(a)
