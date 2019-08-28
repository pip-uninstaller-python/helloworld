class A(object):
    @staticmethod
    def test():
        print('AAA')

class B(object):
    @staticmethod
    def test2():
        print('BBB')
# 在Python中是支持多重继承的，也就是我们可以为一个类同时指定多个父类
#   可以在类名的（）后边添加多个类，来实现多重继承
#   多重继承，会使子类同时拥有多个父类，并且会获取到所有父类中的方法
# 在开发中没有特殊情况，应该尽量避免使用多重继承，因为多重继承会让我们的代码过于复杂
# 如果多个父类中有同名的方法，则会出现在第一个父类中寻找，然后找第二个，然后找第三个。。。
# 前边会覆盖后边的

class C(A,B):  # 多重继承前 class C(B):
    pass

# 类名.__bases__这个属性可以用来获取当前类的所有父类
print(C.__bases__)  # (<class '__main__.B'>,)
print(B.__bases__)  # (<class 'object'>,)
# 多重继承后
print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)
# 同时继承两个类
c = C()
c.test()
c.test2()
