# 类的基本结构
"""
class 类名([父类]):

    公共属性

    # 对象的初始化方法
    def __init__(self, ...):
        ····
    # 其他的方法  # 可以创建多个
    def method_1(self,...):
        ····
    def method_2(self,...):
        ····
"""


class Person:
    """name在类对象当中"""
    # name = '在这里写默认值也不行'
    # 在类中可以定义一些特殊方法(魔术方法)
    # 特殊方法都是以_开头_结尾的方法
    # 特殊方法不需要自己调用
    # 特殊的方法将会在特殊的时刻自动调用
    print('我是代码块中的代码')  # 先执行
    # 学习特殊方法：
    # 1.特殊方法什么时候调用？
    # 2.特殊方法有什么用？

    # p1 = Person()的运行流程
    # 1.创建一个变量
    # 2.在内存中创建一个新对象
    # 实际上它是第一个，忽略：3.执行类中代码块中的代码(只在类定义的时候执行一次)
    # 3.__init__(self)方法执行
    # 4.将对象的ID赋值给变量

    '''
    name在实例对象当中 
    init会在对象创建以后立刻调用
    '''
    # init可以用来向新创建的对象中初始化属性
    # 调用类创建对象时，类后边的所有参数都会依次传递到inti()中
    def __init__(self, name):  # init(初始化)
        # print('init方法执行了~~~')
        # 通过self向新建的对象中初始化属性
        self.name = name  # 将name设置为一个变量

    def say_hello(self):
        print('大家好，我是%s' % self.name)


# 目前来讲，对于Person类来说name是必须的，并且每一个对象中的name属性基本上都是不同的
# 而我们现在是将name属性在定义为对象以后，手动添加到对象中，##这种方式很容易出现错误
# 我们希望，在创建对象时，必须设置name属性，如果不设置对象将无法创建
#   并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成的
# p1 = Person()
# # 手动向对象添加name属性
# p1.name = 'swk'  # 手动容易忘，而且不报错

# p2 = Person()
# p2.name = 'zbj'

# p3 = Person()
# p3.name = 'shs'

# print('*******************')

p1 = Person('swk')  # ''里为init的name变量
p2 = Person('zbj')  # 不写name的话会报错
p3 = Person('shs')  # 将程序简化，把name的值放在Person中

# p1.__init__不能这么做

p2.name = 'zbj'

p1.say_hello()
p2.say_hello()
p3.say_hello()
