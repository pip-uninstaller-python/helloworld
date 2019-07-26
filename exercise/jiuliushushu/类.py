class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 计算平均分(cls):
        平均分 = (cls.语文_成绩 + cls.数学_成绩)/2
        return 平均分

    @classmethod
    def 评级(cls):
        平均分 = cls.计算平均分()
        if 平均分>=90:
            print(cls.学生姓名 + '的评级是：优')
        elif 平均分>= 80 and 平均分<90 :
            print(cls.学生姓名 + '的评级是：良')
        elif 平均分>= 60 and 平均分<80 :
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')
成绩单.录入成绩单()
成绩单.评级()

class 幸运():
    @classmethod
    def 好运翻倍(cls):
        print('好的，我把它存了起来，然后翻了888倍还给你：' + str(cls.幸运数*888))
        # 或者这样写也可以：
        # print('好的，我把它存了起来，然后翻了888倍还给你：%d' % (cls.幸运数*888))
幸运.幸运数 = int(input('你的幸运数是多少？请输入一个整数。'))
幸运.好运翻倍()

class 类():
    @classmethod
    def 打印类属性(cls):
        print(cls.变量)
类.变量 = input('请输入字符串：')
类.打印类属性()

class 类A():
    变量1 = 100
    变量2 = 200
    @classmethod
    def 函数1(cls):
        print(cls.变量1)
        print(cls.变量2)
类A.函数1()

def add_100(num):
    sum = num + 100
    print('计算结果如下：')
    print(sum)
num = 1
add_100(1)


class 加100类():
    def 加100函数(参数):
        总和 = 参数 + 100
        print('计算结果如下：')
        print(总和)
参数 = 1           #这里的加100类()中的加100函数，只使用了外部的参数，没有使用类属性，所以格式上不需要@classmethod和cls。
加100类.加100函数(参数)

一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
def 念诗函数(参数):
    for i in 参数:
        print(i)
念诗函数(一首诗)

一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
class 念诗类():
    def 念诗函数(参数):
        for i in 参数:
            print(i)
念诗类.念诗函数(一首诗)

class 念诗类():
    一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
    @classmethod
    def 念诗函数(cls):
        for i in cls.一首诗:
            print(i)
念诗类.念诗函数()


class 加100类():
    变量 = 100
    @classmethod
    def 加100函数(cls, 参数):
        总和 = cls.变量 + 参数
        print('加100函数计算结果如下：')
        print(总和)
参数 = int(input('请输入一个整数：'))
加100类.加100函数(参数)