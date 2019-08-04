while True:
    try:
        num=int(input('输入一个整数:'))#判断输入是否为整数
    except ValueError:#不是纯数字需要重新输入
        print("输入不是整数！")
        continue
    if num%2==0:
        print('偶数')
    else:
        print('奇数')
    break
