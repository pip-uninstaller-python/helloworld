# 特殊方法，也称为魔术方法
# 特殊方法都是使用_开头和结尾的
# 特殊方法一般不需要手动调用，需要在一些特殊情况下自动执行

# 定义一个Person类
class Person:
    """docstring for Person"""
    def __init__(self,name,age):
        super(Person,self).__init__()
        self.name = name
        self.age = age

    # 这个特殊方法会在尝试将对象转换对字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果
    def __str__(self):
        return 'Person [name = %s,age = %s]'%(self.name,self.age)

    #__repr__这个特殊方法会在对当前对象使用repr()函数时调用
    # 它的作用时指定对象在"交互模式"中直接输出结果
    def __repr__(self):
        return 'Person [name = %s,age = %s]'%(self.name,self.age)

    # object.__lt__(self.other) 小于 <
    # object.__le__(self.other) 小于等于 <=
    # object.__eq__(self.other) 等于 ==
    # object.__ne__(self.other) 不等于 ！=
    # object.__gt__(self.other) 大于>
    # object.__ge__(self.other) 大于等于>=

    # __len__获取对象的长度

    # # object.__bool__(self)


    #__gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较结果
    # 它需要两个参数，一个self表示当前对象，other表示和当前对象比较的对象
    def __gt__(self,other):
        return self.age > other.age
    
    def __bool__(self):
        return self.age>9
        # 创建两个Person类的实例
p1 = Person('sss',10)
p2 = Person('zzz',20)
# 当我们打印一个对象时，实际上打印的时对象中的特殊方法__str__()的返回值
print(repr(p1))  # <__main__.Person object at 0x0000026BBBDBA470>
print(p1>p2)
print(bool(p1))