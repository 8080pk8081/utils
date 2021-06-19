import re
list = ['S0001','2345','A0001']
list2=[]
rr = re.compile('^[A-Za-z][0-9a-z][0-9a-z][0-9j][0-9]$')
for _str in list:
    if rr.findall(_str) != []:
        list2.append(rr.findall(_str)[0])
print(list2)