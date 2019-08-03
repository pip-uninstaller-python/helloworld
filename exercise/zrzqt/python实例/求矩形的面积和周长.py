class Shape:#定义类
    def __init__(self, lenth, width):#矩形的长和宽
        self.lenth = lenth #实例成员
        self.width = width #实例成员
    def Area(self):#矩形的面积
        area = self.width * self.lenth#长乘宽
        return area#返回面积
    def Circumference(self):#矩形的周长
        circumference = 2 * (self.lenth + self.width)#矩形的周长等于长加宽的和乘2
        return circumference#返回周长
class Rectangle(Shape):#定义矩形类
    def __init__(self):
        super().__init__(lenth, width)#调用父类中的__init__方法
if __name__ == '__main__':
    lenth = int(input('请输入长度：'))
    width = int(input('请输入宽度：'))
    result = Rectangle()
    print('面积：', result.Area())#输出
    print('周长：', result.Circumference())#输出
