# coding: utf-8
# 超市里的可乐进行大优惠，每买2瓶送2瓶（买3瓶因为只包含一个2瓶，
# 所以只送2瓶，4瓶可以送4瓶）小明买了n瓶可乐，请你编写一个程序，
# 算算他一共能拿走几瓶可乐。

# 解法:提取了一下规律,可以计算所有类似满减情况

def discounts (n,fun):
    return n+fun(n)

# n 买了几瓶  优惠策略买a瓶赠p瓶
def abovePresent(n,a,p):
    return discounts(n, lambda n: int(n / a) * p)


