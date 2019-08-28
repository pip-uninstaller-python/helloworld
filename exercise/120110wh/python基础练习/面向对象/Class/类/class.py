# 类
# 内置对象不能满足所有需求，所以在开发中经常需要自定义一些对象
"""
    类：简单理解它就相当是一个图纸，在程序中需要根据类来创建对象
    类就是对象的图纸
    也称对象是类的实例（instance）
    如果多个对象是通过一个类创建的，我们称这些对象是一类对象
    int(),float(),bool()str()list()dict()都是类
    a = int(10) 创建一个int类的实例，等价于 a = 10
    自定义的类需要使用大写字母开头，使用大驼峰命名法（帕斯卡命名法）来对类名命名
"""
a = int(10)  # 创建一个int类的实例
b = str('hello')  # 创建一个str类的实例
print(a, type(a))
print(b)


# 定义简单的类
# 使用class关键字来定义类，语法和函数很像
# class 类名（[父类]）：
# 代码块
# <class '__main__.MyClass'>
class MyClass:  # 自定义类
    pass


print(MyClass)

# 使用MyClass创建一个对象
# 使用类来创建对象，就像调用一个函数一样
# <__main__.MyClass object at 0x000002D2A53EB390>
mc = MyClass()  # mc就是通过MyClass创建的对象，mc是MyClass的实例
mc2 = MyClass()
mc3 = MyClass()
# mc,mc2,mc3都是MyClass的实例，他们都是一类对象
print(isinstance(mc2, MyClass))  # isinstance用来 检查一个对象是否是一个类的实例
print(mc, type(mc))
