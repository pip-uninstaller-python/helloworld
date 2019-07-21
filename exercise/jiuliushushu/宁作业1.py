#day1

#1.二进制求和   10101101和11011110    10110111和10011001
num1 = 0b10101101    #0b代表2进制
num2 = 0b11011110
num3 = 0b10110111
num4 = 0b10011001
sum1 = num1 + num2
sum2 = num3 + num4
print(sum1)     #395
print(sum2)     #336

num1 = int("10101101", 2)    #int（需要转换的数字，进制类型）,转换成10进制
num2 = int("11011110", 2)
num3 = int("10110111", 2)
num4 = int("10011001", 2)
sum1 = num1 + num2
sum2 = num3 + num4
print(sum1)    #395
print(sum2)    #336
#2.注释分类及定义
#3.变量类型   int()整数  str()字符串  float()浮点数

#4.定义变量1str1赋值字符串hello,定义str2赋值python，求str1+str2
str1 = "hello"
str2 = "python"
print(str1+str2)     #hello world

#5.变量a="10",b="30",c=a+b,说出c的值和类型，如何让c=“40”
a = 10
b = "30"
c = str(a)+b
print(c)      #字符串c 1030
print(a+int(b))    #整数c 40

#6.输入姓名性别年龄单位联系方式，并用变量分别接收，打印出对应信息
name = input("你的姓名：")
gender = input("你的性别：")
age = int(input("你的年龄："))
unit = input("你的单位：")
tel = int(input("你的联系方式："))
"""定义5个变量并且使用格式化输出"""
print("以下是你的信息：\n姓名：%s  \n性别：%s  \n年龄：%s   \n单位：%s  \n联系方式：%s" %(name, gender, age, unit, tel))
print("以下是你的信息：\n姓名：{}  \n 性别：{}  \n年龄：{}   \n单位：{}  \n联系方式：{}" .format(name, gender, age, unit, tel))

#7.输入一个整数，将该整数翻转输出
a = input("输入一个整数")
print(a[::-1])    #定义字符串a，列表切片 0::从左向右，::-1从右向左





