a = input("请输入带有符号的温度值：")
if a[-1] in ['F','f']:
    C = (eval(a[0:-1])-32)/1.8
    print('转换后的温度是{:.1f}C'.format(C))
elif a [-1] in ['C','c']:
    F = 1.8*eval (a[0:-1]) + 32
    print('转换后的温度是{:.1f}F'.format(F))
else:
    print("输入格式错误")
