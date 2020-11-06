import os

"""os.path  以path为入口，用于操作及处理文件路径"""
print(os.path.abspath(__file__))



"""os.sep : 获取当前目录分割符
window为 '\' linux和unix为/ """
print(os.sep)

"""os.name"""
print(os.name)   #window 为nt内核，Linux和unix则时posix

print(os.getcwd())

print(os.getenv('PATH'))


path1 ='D:/game/bin/gatv.exe'
print(os.path.split(path1))
print(os.path.split(path1)[0])
print(os.path.split(path1)[1])

if os.name =="nt":
	print("操作系统是window")
elif os.name =='posix':
    print("操作系统是Linux或者mac")
else:
    print("看不出来是什么系统哦")

print(os.path.join('d:/',"python/"))