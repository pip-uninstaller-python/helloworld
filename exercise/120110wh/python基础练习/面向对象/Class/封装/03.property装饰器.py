class Person:
    def __init__(self,name):
        self._name = name

    # property 装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器 以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名一样的
    @property
    def name(self):
        print('get方法执行了~~~~')
        return self._name

    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, name):
        self._name = name
p = Person('asd')
print(p.name)
p.name = '153215'
print(p.name)