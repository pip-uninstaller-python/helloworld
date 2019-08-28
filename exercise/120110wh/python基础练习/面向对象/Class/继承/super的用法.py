class Animal:

    def __init__(self,name):
        self._name = name

    def yao(self):
        print('动物咬人~~~')

    def run(self):
        print('动物奔跑~~~')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

class Dog(Animal):
    def __init__(self,name,age):
        # 希望可以直接调用父类的__init__来初始化类中定义的属性
        # super()可以获取当前类的父类，并且通过super()返回对象调用父类方法，不需要传递self
        super().__init__(name)
        self._age = age

    def dark():
        print('汪汪汪！！！')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

d = Dog('旺财',18)
print(d.name)
print(d.age)