# 雪景艺术绘图
# 图形艺术背景是黑色，分为上下两个区域，上方是漫天彩色雪花，下方是由远及近的灰色横线渐变
# 运用了随机元素，如雪花位置、颜色、大小、花瓣数目、地面灰色线条长度、线条位置等，用到了turtle和random库

# 注：图形艺术程序往往动画时间较长，可以在主程序调用Tracer(False)函数关闭动画效果，从而一次性绘制所有效果

# 第一步：构建图的背景，窗体大小为800*600，颜色为black，然后定义上方雪花绘制函数drawSnow()和下方雪地绘制函数draeGround()

# 第二步：绘制雪花效果，为体现艺术效果，drawSnow()函数首先隐藏画笔，设置画笔大小、绘制速度，
# 然后使用for循环绘制100朵雪花，为了使雪花颜色随机，使用random()函数生成画笔颜色rgb值
# 这里采用turtle库默认的0~1浮点数RGB取值，在指定区域随机选择坐标绘制雪花，利用randint(-350，350)生成随机数
# 上方区域定义为x坐标范围(-350,350),y坐标范围为(1,270)内的区域，雪花大小为snowsize，雪花花瓣数dens都分别设为一定范围内的随机数
# 最后通过for循环绘制出多彩雪花

# 第三步：绘制雪地效果。drawGround()函数使用for循环绘制地面400道小横线，
# 画笔大小pensize、位置坐标x,y、线段长度均通过ranint()作为随机数生成。
# 由于小横线的灰度呈现由远及近的效果，因此r、g、b的值应根据y坐标进行变化；
# 灰色的r、g、b值颜色相等，为了控制在0~1之间，它们的计算方式均为-y/280


from turtle import *
from random import *


def drawSnow():
    hideturtle()
    pensize(2)
    for i in range(100):
        r,g,b = random(),random(),random()
        pencolor((r,g,b))
        penup()
        setx(randint(-350,350))
        sety(randint(1,270))
        pendown()
        dens = randint(8,12)
        snowsize = randint(10,14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)

def drawGround():
    hideturtle()
    for i in range(400):
        pensize(randint(5,10))
        x = randint(-400,350)
        y = randint(-280, -1)
        r,g,b = -y/280,-y/280,-y/280
        pencolor((r,g,b))
        penup()
        goto(x,y)
        pendown()
        forward(randint(40,100))

setup(800, 600, 200, 200)
tracer(False)
bgcolor("black")
drawSnow()
drawGround()
done()