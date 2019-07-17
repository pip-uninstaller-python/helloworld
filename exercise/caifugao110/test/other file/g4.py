# print("我叫%s今年%d岁!" % ('小明', 10))
# print("%s+%s=%s" % (2, 3, 5))
# print("please input the first numble")
# a = input()
# print("please input the second numble")
# b = input()
# c = a if a > b else b
# print(c)
# str1 = 'adSFSGSGRWasfasf'
# print(str1.isspace())
# print(len(str1))
# print(str1.lower())
# print(str1.swapcase())

# list1 = list2 = ['Google', 'Runoob', 1997, 2000]
# print("原始列表 : ", list1)
# del list1[3]
# print("删除第三个元素 : ", list1)
# list1[1] = 'Baidu'
# print("修改第二个元素 : ", list1)
# list3 = [list1, list2]
# list4 = list1 + list2
# print(list3[0][0])
# print(list4)
# print(list4.count(1997))
# list4.reverse()

# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x[0][0])
# a = [1, 3, 5]
# b = [2, 4, 6]
# c = [a[i]+b[i] for i in range(len(a))]
# print(c)
# print([x * y for x in a for y in b])

# a = ('gao', 'jian', 'he', 'yanlin',)
# print(a[1])
# b = len(a)
# print(b)
# c = list(a)
# c[1] = 'tianbao'
# print(tuple(c))
# name1 = a[0] + a[1]
# name2 = a[2] + a[3]
# print(name1, "\n", name2)

# a = {"name1": "gaojian","name2":"heyanlin"}
# a["name1"] = "gaotianbao"
# print(a, '\n', len(a))
# print("name1" in a)

# students = {}
# write = 1
# while write:
#     name = str(input('输入名字:'))
#     grade = int(input('输入分数:'))
#     students[str(name)] = grade
#     write = int(input('继续输入？\n 1/继续  0/退出'))
# print('name  grade  rate'.center(20, '-'))
# for key, value in students.items():
#     if value >= 90:
#         print('%s %s  A'.center(20, '-') % (key, value))
#     elif 89 > value >= 60:
#         print('%s %s  B'.center(20, '-') % (key, value))
#     else:
#         print('%s %s  C'.center(20, '-') % (key, value))

# a = 1
# while a < 7:
#     print(a)
#     a += 1
#     print()

# n = int(input("请输入一个整数n:"))
# b = {0: 0, 1: 1}
#
#
# def fib(n):
#     write = 1
#     while write:
#         if n in b:
#             return b[n]
#         else:
#             temp = fib(n-1) + fib(n-2)
#             b[n] = temp
#             return temp
#             print(input("countinue or exit \n 1->countinue \n 0->exit"))
#
#
# for i in range(n):
#     print(fib(i+1), end=" ")

# a, b = 0, 1
# n = int(input("please input a numble:"))
# while b < n:
#     print(b)
#     a, b = b, a + b

# a = ["gao", "jian", "he", "yan", "lin"]
# # for i in range(len(a)):
# #     print(i, a[i])
# for i in a:
#     print(i)

"""
输出n以内所有质数
"""
# a = []
# n = int(input("please input a numble:"))
# for x in range(2, n+1):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#         else:
#             a.append(y)
# print("n以内的质数有", a)

"""
输出九九乘法表
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j), end=" ")
#     print()

"""
冒泡排序
"""
# def paixu(li):
#     for ad in range(len(li) - 1):
#         for x in range(len(li) - 1 - ad):
#             if li[x] < li[x + 1]:
#                 max = li[x]
#                 li[x] = li[x + 1]
#                 li[x + 1] = max
#             else:
#                 max = li[x + 1]
#     print(li)
#
#
# paixu([41, 23344, 9353, 5554, 44, 7557, 6434, 500, 2000])

'''
输出n以内的所有裴波纳契数
'''
# n = int(input("请输入一个整数n："))
# n0, n1 = 0, 1
# while n1 < n:
#     print(n1, end=" ")
#     n0, n1 = n1, n0+n1




