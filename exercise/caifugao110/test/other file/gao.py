# a =1.232323232
# # print(round(a,2))

# import sys
# sys.setrecursionlimit(100)

def add(a,b):
    result = a + b
    return result
def print_code(code):
    print(code)
# x = add(3,5)
# y = print_code('python')
# print(x,y)

# x = 1
# s = 1
# while x <= 100:
#     s = s + x
#     x = x + 1
# 2019.06.29
# 阶乘函数


# def jc(x):
#     s = 1
#     c = int(x) + 1
#     for t in range(1,c,1):
#         s = s * t
#     return s
#
#
# print('input the number')
# a = input()
# b = jc(a)
# print(b)


# def dianji(dianjimao='obara',dianjibing='sgmc',dianjijietou='richan'):
#     print('电极帽标准是：' + dianjimao)
#     print('电极柄标准是：' + dianjibing)
#     print('电极接头标准是：' + dianjijietou)
#     print('~~~~~~~~~~~~~~~~~~~~~~')
#
#
# dianji()
# dianji('一汽','五菱','上汽')


# class Student():
#     name = ''
#     age = 0
#
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))


import re
a = 'java 8 98python_1php'
r = re.findall('[a-z]{3,6}?', a)
print(r)
