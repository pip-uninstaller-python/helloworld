'''
以后别用这个程序
import time
time_01 = time.time()   #起始时间
a = ""
for i in range(1000000):
    a+="str"

time_02 = time.time()   #终止时间
print("运行时间为="+str(time_02-time_01))


#下面是join()函数的时间

time_03 = time.time()   #起始时间
li = []     #这里li是一个壳
for i in range(1000000):
    li.append("str")
    
b = "".join(li)
time_04 = time.time()   #终止时间
print("join()运行时间为="+str(time_04-time_03))
'''
