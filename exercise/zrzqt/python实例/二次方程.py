#二次方程式ax**2 +bx +c =0
#a、b、c用户提供，为实数，a≠0
#导入cmath(复杂数学运算)模块
import cmath
a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))
#计算
d = (b**2) - (4*a*c)
#两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('结果为{0} 和 {1}'.format(sol1,sol2))
#使用了 cmath (complex math) 模块的 sqrt() 方法 来计算平方根。
