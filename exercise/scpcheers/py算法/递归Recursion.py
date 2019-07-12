
# 递归
# 抱着抱着抱着我的小鲤鱼得我得我得我


def func(n):
    if n > 0:
        func(n-1)
        print(n)


def text(n):
    if n > 0:
        print("抱着", end='')
        text(n-1)
        print("的我", end='')
    else:
        print("我的小鲤鱼", end='')


# 斐波那契数列： 1 1 2 3 5 8 13 21
def f(n):
    # 判断n值不为负数
    if n <= 0:
        print("n值必须大于1！")
    else:
        i = 1


if __name__ == '__main__':
    # func(5)
    text(5)
