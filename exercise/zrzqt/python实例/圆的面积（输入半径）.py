#计算圆的面积
PI =3.14159265
r = input("输入一个半径r的值：")
if r.isdigit():#判断是否是数字字符串
    s = PI * pow(float(r),2)
    print("半径为{}的圆的面积为:{:.3f}".format(r,s))
else:
    print("输入错误！")
