a = 0
while a < 5:
    a = a + 1
    print(a)

while False:
    print('while False')

if False:
    print('if False')

if True:
    print('if True')

print(3<5)
print(3>5)
print('长安'=='长安')
print('长安'!='金陵')

password = input('请输入密码：')
if password == '007':
    print('密码正确！')
else:
    print('密码错误！')

if 1:
    print('熊猫')


print('以下数据判断结果都是【假】：')
print(bool(False))
print(bool(0))
print(bool(''))
print(bool(None))
print('以下数据判断结果都是【真】：')
print(bool(True))
print(bool(1))
print(bool('abc'))

a = 1
b = -1
print('以下是and运算')
if a==1 and b==1:    # 【b实际上是-1】
    print('True')
else:
    print('False')

print('以下是or运算')
if a==1 or b==1:  # 【b实际上是-1】
    print('True')
else:
    print('False')

list = [1,2,3,4,5]
a = 1
# 判断“a是否在列表list中
print(bool(a in list))
print(bool(a not in list))