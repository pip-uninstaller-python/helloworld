def menu(appetizer, course, *barbeque, dessert='绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主菜：' + course)
    print('一份甜品：' + dessert)
    for i in barbeque:
        print('一份烤串：' + i)
menu('话梅花生', '牛肉拉面', '烤鸡翅', '烤茄子', '烤玉米')

def chide(xiaocai,zhushi,tianpin='黑森林可乐',*shaokao):
    print('一盘小菜：'+xiaocai)
    print('主食来啦：'+zhushi)
    print('一份甜品：'+tianpin)
    for i in shaokao:
        print('烧烤之一：'+i)
chide('炒豆苗','馒头','樱桃布丁','羊肉串','肉筋','板筋','烤韭菜')

def niduoda(age):
    if age < 12:
        return '哈，是祖国的花朵啊'
    elif age < 25:
        return '哇，是小鲜肉呢'
    else:
        return '嗯，人生才刚刚开始'
print(niduoda(30))

def people(name):
    print("我喜欢"+ name +"的脸")
people("迪丽热巴")
def people2(name2):
    print("我喜欢" + name2 +"的身材")
people2("陈乔恩")

def face(name):
    return name + '的脸蛋'
#该函数返回字符串'XXX的脸蛋'
def body(name):
    return name + '的身材'
#分别调用face()和body()函数
print('我的梦中情人：'+face('李若彤') +' + ' + body('林志玲'))

def face(name):
    return name + '的脸蛋'
def body(name):
    return name + '的身材'
def main(dream_face,dream_body):
    return '我的梦中情人：' + face(dream_face) + ' + ' + body(dream_body)
print(main('李若彤','林志玲'))
print(main('新垣结衣','长泽雅美'))

def lover(name1,name2):
    face = name1 + '的脸蛋'
    body = name2 + '的身材'
    return face,body
a=lover('李若彤','林志玲')
print('我的梦中情人：'+a[0]+' + '+a[1])
print(type(a))

def fun():
    a ='I am coding'
print(fun())   #没有return的函数返回None

def fun():
    a='I am coding'
    return a
print(fun())

def fun():
  return 'I am coding.'
  return 'I am not coding.'
print(fun())