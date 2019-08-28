# 多态
class A:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

class B:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

class C:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

a = A('swk')
b = B('zbj')
c = C('shs')
#定义一个函数
def say_hello(obj):
    print('你好 %s'%obj.name)
def say_hello2(obj):
    if isinstance(obj,A):
        print('你好 %s'%obj.name)
say_hello(c)
say_hello2(a)
