# !/usr/bin/python3

#排序函数sorted
# def hanshu(s1, s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1 < u2:
#         return -1
#     if u1 > u2:
#         return 1
#     return 0

# print (sorted(['Bomb', 'army', 'carry', 'edit']), hanshu)

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


a = sorted(['bob', 'about', 'Zoo', 'Credit'])
b = list(a)
print (b)



# import math
# def is_sqr(x):
#     return math.sqrt(x) % 1 == 0

# a = filter(is_sqr, range(1, 101))
# newList = list(a)
# print(newList)

# def is_odd(n):
#     b = int(math.sqrt(n))
#     return b*b == n
 
# tmplist = filter(is_odd,range(1,101))
# newlist = list(tmplist)
# print(newlist)