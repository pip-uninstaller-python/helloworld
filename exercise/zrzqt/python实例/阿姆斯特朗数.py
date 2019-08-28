#python检测用户输入的数字是否为阿姆斯特朗数
#获取用户输入的数字
num = int(input('请输入一个数字：'))
#初始化变量 sum
sum = 0
#指数
n = len(str(num))
#检测
temp = num
while temp > 0:
   digit = temp %10
   sum += digit ** n
   temp //=10
#输出结果
if num == sum:
   print (num,'是阿姆斯特朗数')
else:
   print(num,'不是阿姆斯特朗数')
#如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
