"""
输出n以内所有质数
"""
# a = []
# n = int(input("please input a numble:"))
# for x in range(2, n+1):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#     else:
#         a.append(x)
# print("n以内的质数有", a)

'''
格式化测试
'''
a = [1, 3, 5, 7, 9]
for i in range(len(a)):
    print('{0}对应的值为：{1}'.format(i, a[i]))

'''
文件读写
'''
# f = open("C:/Users/Administrator.SC-201904210026/Desktop/tese.txt", "w")
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# f.close()
