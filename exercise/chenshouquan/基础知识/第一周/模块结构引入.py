#模块是Python中最高级别组织单元，它将程序代码和数据封装起来以便重用，模块的作用1.代码重用2.实现共享服务和数据。
#导入从本质上讲，就是再一个文件中载入另外一个文件，并且能够读取那个文件的内容。一个模块内的内容通过这样的方法其属性（object，attribute）能够被外界使用。
#Lib文件夹下的文件就是模块存储地方
import random#引入生成随机数的模块，import+模块名

a=random.random()#随机数小数
b=random.choice(["张三","李四","王五"])#点名随机出
print(a)#直接出来不设置小数位的
print(round(a,2))#小数点太多了保留2位
print(b)

#
from random import choice,random#引入random模块choice和random方法中间用逗号隔开
print(choice([1,2,3,4,5,6]))#
print(random())

from random import*#引入random模块所有方法 from 模块 ipmort*
print(random())
print(randint(1,10))#1-10随机整数
