#用户输入
x = input('输入x值：')
y = input('输入y值：')
#创建临时变量，并交换
temp = x
x = y
y = temp
print('交换后x的值为：{}'.format(x))
print('交换后y的值为：{}'.format(y))
#我们创建了临时变量temp，并将x的值存储在temp变量中，接着将y值赋给x，最后将temp赋值给y变量。
