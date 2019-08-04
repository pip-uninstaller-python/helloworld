#通过用户输入数字计算阶乘
#获取用户输入的数字
num = int(input('请输入一个数字：'))
factorial = 1
#查看数字是负数，0 或 正数
if num < 0:
    print('抱歉，负数没有阶乘')
elif num == 0:
    print('0的阶乘为1')
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print('%d的阶乘为%d'%(num,factorial))
