# coding: utf-8
# 超市里的可乐进行大优惠，每买2瓶送2瓶（买3瓶因为只包含一个2瓶，
# 所以只送2瓶，4瓶可以送4瓶）小明买了n瓶可乐，请你编写一个程序，
# 算算他一共能拿走几瓶可乐。
'''
def buy():
    num = input("输入购买数量：")
    n = int(num)
    if (n % 2 == 0):
        return int(num)*2
    else:
        n = n - 1
        return n*2+1


num = buy()
print(num)
'''

# 超市里的可乐进行大优惠，每买p瓶送q瓶（如：买2送2，买3瓶因为只包含一个2瓶，
# 所以只送2瓶，4瓶可以送4瓶）小明买了n瓶可乐，请你编写一个程序，
# 算算他一共能拿走几瓶可乐。
def buy(p, q):
    num = input("输入购买数量：")
    n = int(num)
    return n + int(n / p) * q
    # if n % p == 0:
    #     return n + n / p * q
    # else:
    #     return n + (n - 1) / p * q


num = buy(4, 1)
print(num)