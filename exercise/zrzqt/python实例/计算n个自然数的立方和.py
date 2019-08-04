#计算1³+2³+3³+4³+...+n³
#定义立方和的函数
def sum0fSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i*i*i
    return sum
#调用函数
n = 5
print(sum0fSeries(n))
