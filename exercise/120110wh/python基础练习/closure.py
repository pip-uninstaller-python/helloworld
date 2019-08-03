
##形成闭包的要点
#1.函数嵌套
#2.将内部函数作为返回值返回
#3.内部函数必须要使用到外部函数的变量
def make_averager():
    #创建一个列表，用来保存数值
    nums = []

    def averager(n):
        #将n添加到列表中
        #引用变量，不引用没有意义
        nums.append(n)

        return sum(nums)/len(nums)
        #求平均值

    return averager
#调用函数
##print(nums)
#将会报错，nums内局部变量
averager = make_averager()
print(averager(20))
print(averager(20))
print(averager(40))
print(averager(20))


