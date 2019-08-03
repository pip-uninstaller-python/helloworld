import cmath
a = float(input('请输入一个实数字:'))
b = float(input('请输入一个虚数字:'))
num_sqrt = cmath.sqrt(complex(a,b))
print('{0:0.3f}+{1:0.3f}j的平方根为 {2:0.3f}+{3:0.3f}j'.format(a,b,num_sqrt.real,num_sqrt.imag))
#求复数的平方根
