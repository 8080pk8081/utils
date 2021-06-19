import os
import os.path
import time
import glob     #文件操作相关模块，用它可以查找符合自己目的的文件
# 删除已有测试cmd脚本
path = r"E:\\monkey_test\\"
for file in glob.glob(os.path.join(path, '*.cmd')):  #路径拼接：E:\\monkey_test\\*.cmd  查到出该路劲下所有.cmd的文件
  os.remove(file)

os.system("cls")  #os.system ('')等于在cmd窗口内输入命令行     os.system("cls")具有清屏功能
rt = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的结果
n = len(rt) - 2
print ("当前已连接待测手机数为：" + str(n))
aw =input("是否要开始你的monkey测试，请输入(yes or no): ")

if aw == 'yes':
 print ("monkey测试即将开始....")
 count = input("请输入你要进行的monkey测试次数: ")
 testmodel = input("请输入你是要进行单次测试还是多次连续测试，请输入(1-代表单次测试，2-代表多次连续测试): ")
 ds = range(n)
 for i in range(n):
     nPos = rt[i + 1].index(r"\t")
     ds[i] = rt[i + 1][:nPos]
     dev = ds[i]
     promodel = os.popen(
         "adb -s " + dev + ' shell cat /system/build.prop | find "ro.product.model="').readlines()  # 获取手机型号
     #modelname = ('').join(promodel)  # 将list转为字符串
     modelname = promodel[0] #从list中取出第一个值
     model = modelname[17:].strip('\r\n')
     proname = os.popen(
         "adb -s " + dev + ' shell cat /system/build.prop | find "ro.product.brand="').readlines()  # 获取手机名称
     roname = proname[0]
     name = roname[17:].strip('\r\n')
     packagename = os.popen(
         "adb -s " + dev + ' shell pm list packages | find "xxx"').readlines()
     package = packagename[0]
     pk = package[8:].strip('\r\n')
     if pk == 'com.xxx':
         filedir = os.path.exists("E:\\monkey_test\\")
         if filedir:
             print ("File Exist!")
         else:
             os.mkdir("E:\\monkey_test\\")
         devicedir = os.path.exists("E:\\monkey_test\\" +name + '-' + model + '-' + dev)
         if devicedir:
             print ("File Exist!")
         else:
             os.mkdir("E:\\monkey_test\\" +name + '-' + model + '-' + dev)  # 按设备ID生成日志目录文件夹
         wl = open("E:\\monkey_test\\" +name + '-' + model + '-' + ds[i] + '-logcat' + '.cmd', 'w')
         #wl.write('adb -s ' + dev + ' logcat -v time ACRA:E ANRManager:E System.err:W *:S')
         wl.write('adb -s ' + dev + ' logcat -v time *:W')
         wl.write('> E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\logcat_%random%.txt\n')
         wl.close()
         if testmodel == '1':
             wd = open("E:\\monkey_test\\" +name + '-' + model + '-' + ds[i] + '-device' + '.cmd', 'w')
             wd.write(
                      'adb -s ' + dev + ' shell monkey -p com.xxx --monitor-native-crashes --ignore-crashes --pct-syskeys 5 --pct-touch 55 --pct-appswitch 20 --pct-anyevent 20 --throttle 200 -s %random% -v ' + count)  # 选择设备执行monkey
             wd.write('> E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\monkey_%random%.txt\n')
             wd.write('@echo 测试成功完成，请查看日志文件~')
             wd.close()
         elif testmodel == '2':
             wd = open("E:\\monkey_test\\" +name + '-' + model + '-' + ds[i] + '-device' + '.cmd', 'w')
             wd.write(':loop')
             wd.write('\nset /a num+=1')
             wd.write('\nif "%num%"=="4" goto end')
             wd.write(
                      '\nadb -s ' + dev + ' shell monkey -p com.xxx --monitor-native-crashes --ignore-crashes --pct-syskeys 5 --pct-touch 55 --pct-appswitch 20 --pct-anyevent 20 --throttle 200 -s %random% -v ' + count)  # 选择设备执行monkey
             wd.write('> E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\monkey_%random%.txt\n')
             wd.write('@echo 测试成功完成，请查看日志文件~')
             wd.write('\nadb -s '+ dev +' shell am force-stop '+ pk)
             wd.write('\n@ping -n 15 127.1 >nul')
             wd.write('\ngoto loop')
             wd.write('\n:end')
             wd.close()
     else:
         print("请确认待测手机"+name + '-' + model +"未安装com.xxx~")

 # 执行上述生成的cmd脚本path='E:\\monkey_test\\'
 for file in os.listdir(path):
     if os.path.isfile(os.path.join(path, file)) == True:
         if file.find('.cmd') > 0:
             os.system('start ' + os.path.join(path, '"' + file + '"'))  # dos命令中文件名如果有空格，需加上双引号
             time.sleep(1)
elif aw == 'no':
 print('请重新确认所有待测手机是否已通过adb命令连接至pc!')
else:
 print("测试结束，输入非法，请重新输入yes or no！")