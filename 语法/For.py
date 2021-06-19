#整数次数控制
for i in range (5):
    print(i)
print("-"*20)
for j in range(1,5):
    print(j)
print("-"*20)

for z in range(1,5,2):
    print(z)
print("-"*20)

for a in [1,4,6,7]:
    print(a)
print("-"*20)

for h in range(9):
    print(h)
    if h ==4:
        break
else:
    print("for-else:for循环完整执行后，else才会被执行")
print("-"*20)

for h in range(9):
    print(h)
    if h ==10:
        break
else:
    print("for-else:for循环完整执行后，else才会被执行")
print("-"*20)

for i in range(4):
    if i == 2:
        continue
    print(i)
