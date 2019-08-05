sentence = '从前有座山，'
def mountain():
    print('山里有座庙，')
class Temple:
    sentence = '庙里有个老和尚，'
    @classmethod
    def reading(cls):
        print('在讲故事，')
class Story:
    sentence = '一个长长的故事。'
    def reading(self):
        print('讲的什么故事呢？')
for i in range(10):
    print(sentence)
    mountain()
    print(Temple.sentence)
    Temple.reading()
    A = Story()
    print(A.sentence)
    A.reading()
    print()


import test  # 导入test模块
print(test.a)  # 使用“模块.变量”调用模块中的变量
test.hi()  # 使用“模块.函数()”调用模块中的函数
print(test.Go1.a)   # 使用“模块.类.变量”调用模块中的类属性
test.Go1.do1()  # 使用“模块.类.函数()”调用模块中的类方法
A = test.Go2()  # 使用“变量 = 模块.类()”实例化模块中的类
print(A.a)  # 实例化后，不再需要“模块.”
A.do2()  # 实例化后，不再需要“模块.”

a = '我是模块中的变量a'
def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')
class Go1:  # 如果没有继承的类，class语句中可以省略括号，但定义函数的def语句括号不能省
    a = '我是类1中的变量a'
    @classmethod
    def do1(cls):
        print('函数“do1”已经运行！')
class Go2:
    a = '我是类2中的变量a'
    def do2(self):
        print('函数“do2”已经运行！')
print(a)  # 打印变量“a”

hi()  # 调用函数“hi”
print(Go1.a)  # 打印类属性“a”
Go1.do1()  # 调用类方法“Go1”
A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”