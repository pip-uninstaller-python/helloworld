def demo(m,n):#求最大公约数和最小公倍数 定义函数
    p = m*n #变量p=变量m*变量n
    while m%n != 0:#循环执行，当 m%n !≠0 结束
        m,n=n,m%n
    return (n,p//n)
a = int(input('请输入其中一个整数：'))#输入a的值
b = int(input('请输入另一个整数：'))#输入b的值
c = demo(a,b)#调用函数 得到值
print(c)#输出c

