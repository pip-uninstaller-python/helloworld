# 封装是面向对象的三大特性之一
# 封装指的是隐藏对象中一些不希望被外部所访问到的属性和方法
# 如何隐藏一个对象中的属性
# - 将对象属性名，修改为一个外部不知道的名字
# 如何获取（修改）对象中的属性？
# - 需要提供一个getter和setter方法使外部可以访问到属性
# -- getter 获取对象中的指定属性(get_属性名)
# -- setter 用来设置对象的指定属性(set_属性名)
"""
# 第一步隐藏了属性名，使调用者无法随意的修改对象中的属性
# 第二步使用getter获取，使用setter设置。很好的控制的属性是否是只读的
"""
# 使用封装，确实增加了类的定义的复杂程度，但是它也确保了数据的安全性
# 如果希望属性是只读的，则可以直接取掉setter方法
# 如果希望属性不能被外部访问，则可以直接去掉getter方法
# 第三 使用setter方法设置属性，可以增加数据的验证，确保数据是正确的
# 使用getter方法获取属性，使用setter方法设置属性
#   可以在读取属性和修改属性的同时做一些其他处理


class Dog:
    """
        表示狗的类
    """
    def __init__(self, name: object, age) -> object:
        """
        :type name: object
        """
        self.hidden_name = name
        self.hidden_age = age
    def say_hello(self):
        print("大家好，我是%s" % self.hidden_name)

    def get_name(self):
        """
            get_name()用来获取对象的name属性

        :return:
        """
        return self.hidden_name

    def get_age(self):
        return self.hidden_age

    def set_name(self, name):
        self.hidden_name = name

    def set_age(self, age):
        if age > 0:
            self.hidden_age =age


# 没封装，怎么修改都可以
## d = Dog('旺财')
## print(d.name)
## d.name = '小黑'
## print(d.name)
# ----------------------------------- #
d = Dog('小黑', '8')
d.hidden_name = '小白'
d.say_hello()
print(d.get_name())

#调用setter来修改name属性
d.set_name('小红')
d.set_age(-10)  # 不是大于零则报错
print(d.get_name(),d.get_age())