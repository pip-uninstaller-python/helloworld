# -*- coding: utf-8 -*-
# 开发团队   ：pip uninstall python
# 开发人员   ：breakmyself
# 开发时间   ：2019/8/26  11:56 
# 文件名称   ：escapes_depth.PY
# 开发工具   ：PyCharm
#github主页：https://github.com/breakmyself
"""
转义字符：
\b:退格符
\n:换行符
\r:回车符
\t:制表符
\":双引号
\':单引号
\\:反斜线
"""
s = 'Hello\nCharlie\nGood\nMorning'
print(s)
s2 = '商品名\t\t\t\t单价\t\t数量\t\t总价'
s3 = '疯狂Java讲义\t108\t\t\t2\t\t216'
print(s2)
print(s3)
"""
字符串格式化： %
"""
price = 108
print("The book's price is %s" %price)

user = 'Charli'
age = 8
print("%s is a %s years old boy" %(user,age))
"""
转换说明符
d,i  转为带符号的十进制形式的整数
o ：转换为带符号的八进制形式的整数
x：转为带符号的十六进制形式的整数
X：转换为带符号的十六进制形式的整数
e:转换为科学计数法表示的浮点数（e小写）
E：转换为科学计数法表示的浮点数
f,F:转换成十进制形式的浮点数
g:智能选择使用f或e格式
G：智能选择使用F或E格式
C：转换为单位字符（只接受整数或单字符字符串）
r：使用repr()将变量或表达式转换为字符串
s:使用str()将变量或者表达式转换为字符串
"""
num = -28
print("num is:%6i" %num)
print("num is:%6d" %num)
print("num is:%6o" %num)
print("num is:%6x" %num)
print("num is:%6X" %num)
print("num is:%6s" %num)
"""
-:指定左对齐
+：表示数值总要带着符号(正数带"+",负数带"-")
0：表示不补充空格，而是补充0

"""
num2 = 30
#最小宽度为0，左边补0
print("num2 is : %06d" % num2)
#最小宽度为6，左边补0，总带上符号
print("num2 is: %+06d" % num2)
#最小宽度为6，左对齐
print("num2 is : %-6d" % num2)

#转换浮点数
my_value = 3.001415926535
#最小宽度为8，小数点后保留3位
print("my_value is :%8.3f" % my_value)
#最小宽度为8，左边补0，小数点保留3位
print("my_value is %08.3f" %my_value)
#最小宽度为8，保留小数点3位，左边补0，始终带字符
print("my_value is %+08.3f "  %my_value)
the_name = "Charlie"
print("the_name is: %.3s" % the_name)
#只保留2个字符，最小宽度为10
print("the_name is: %10.2s" % the_name)


