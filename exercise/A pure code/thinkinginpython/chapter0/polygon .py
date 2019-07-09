import turtle
import math


# 正四边形
def square(func, len):
    for i in range(4):
        func.fd(len)
        func.lt(90)


# square(turtle.Turtle(), 200)


# 正n边形
def polygon(func, n, len, angle=360):
    for i in range(n):
        func.fd(len)
        func.lt(angle / n)


# polygon(turtle.Turtle(), 6, 100)


# 近似圆
def circle(func, r):
    n = 100
    polygon(func, n, 2 * math.pi * r / n)


# circle(turtle.Turtle(),100)

# 不完整圆1
def arc1(func, r, angle):
    arc_len = 2 * math.pi * r * angle / 360
    n = 100
    cir_len = arc_len / n
    cir_angle = angle / n
    for i in range(n):
        func.fd(cir_len)
        func.lt(cir_angle)


# arc1(turtle.Turtle(), 100, 90)


# 不完整圆2
def arc2(func, r, angle):
    arc_len = 2 * math.pi * r * angle / 360
    n = 100
    polygon(func, n, arc_len / n, angle)


arc2(turtle.Turtle(), 100, 200)
