# 尝试自定义一个表示狗的类（Dog）
"""
属性：
    age
    gender
    height
方法：
    jiao()
    yao()
    run()
"""


class Dog:
    """
    表示狗的类
    """
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    @staticmethod
    def jiao():
        """
            狗叫的方法
        """
        print('汪汪汪~~~~')

    @staticmethod
    def yao():
        """
            狗咬的方法
        """
        print("咬你~~~~")

    def run(self):
        print("{}快乐的奔跑着".format(self.name))


# 缺点：值可以任意修改！
d = Dog('旺财', '8', 'male', 30)
print("姓名：{}\n年龄：{}\n性别：{}\n身高：{}".format(d.name, d.age, d.gender, d.height))
d.run()
d.jiao()
d.yao()
