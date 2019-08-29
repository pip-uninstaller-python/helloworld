from random import *

# # 生成[0.0,1.0)之间的随机小数
# print(random())

# # seed的使用 -- 种子
# seed(0)
# print(random())
# seed(0)  # 在此设置相同的种子，则后续产生相同的随机数
# print(random())

# # 随机生成[1,10]的随机整数
# randint(1,10)

# # 返回[0,16)内0,2...14的随机数
# a = randrange(0,18,2)

# # 随机生成[10.1,100.2]之间的随机小数，可等于b
# uniform(10.1,100.2)

# # 从一个序列类型变量中随机返回一个元素
# choice('python123')

# # 随机排序一个序列类型变量
# ls = [1,2,3,4,5,6,7]
# shuffle(ls)
# print(ls)

# # 从ls2中随取出三个值，ls2可以是列表、元组、集合、字符串等，返回列表类型
# ls2 = [1,2,3,4,5,6]
# print(sample(ls2, 3))
