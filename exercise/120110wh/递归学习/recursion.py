#递归问题就是分治思想，1-2-4-8-16逐层返回
#字符串反转递归方法
'''
def rvs(n):
    if n == "":
        return n
    else:
        return rvs(n[1:]) + n[0]
print(rvs(str(input(""))))
'''
#字符串反转迭代方法
'''
s = input("")
result = s[::-1]
print(result)
'''
#计算阶乘递归的方法
'''
def jiecheng(n):
    if n == 0:
        return 1
    else:
        return n * jiecheng(n-1)
print(jiecheng(6))
'''
#计算阶乘迭代的方法
'''
def factorial(n):
    result = 1
    for i in range(n):
        result *= (i+1)
    return result
number = int(input())
a = factorial(number)
print(a)
'''
#斐波那契数列递归方法
'''
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(35))
'''
#斐波那契数列迭代方法
'''
n = int(input(""))
An=(1/pow(5,0.5))*(pow(((1+pow(5,0.5))/2),n)-pow(((1-pow(5,0.5))/2),n))#斐波那契数列通项公式
print("{}:{:.0f}".format(n,An))
'''
#汉诺塔递归方法1
'''
count = 0
def hanoi(n,x,y,z):# 左 中 右
    global count
    if n == 1:
        print("{}:{}->{}".format(1,x,z))
        count += 1
    else:
        hanoi(n-1,x,y,z)
        print("{}:{}->{}".format(n,x,z))
        count += 1
        hanoi(n-1,y,x,z)
hanoi(5,"x","y","z")
print("{}次".format(count))
'''
#汉诺塔递归方法2
'''
count = 0
def hanoi(n,a,b,c): #^^^a：初始柱^^^b：中转柱^^^c：目标柱^^^
    global count
    if n == 1 :
        print("{}:{}->{}".format(1,a,c))
        count += 1
    else:
        hanoi(n-1,a,b,c)
        print("{}:{}->{}".format(n,a,c))
        count += 1
        hanoi(n-1,b,a,c)
hanoi(5,"A","B","C")
print(count)
'''