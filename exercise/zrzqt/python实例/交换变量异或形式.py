#交换变量
x = int(input('输入x值：'))
y = int(input('输入y值：'))
x = x ^ y
y = x ^ y
x = x ^ y
print('交换后的x的值为:',x)
print('交换后的y的值为:',y)
