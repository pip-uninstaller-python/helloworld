#用户输入
x = input('输入x值：')
y = input('输入y值：')
#不使用临时变量
x,y = y,x
print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))
