import turtle,time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    turtle.pencolor("NavajoWhite1")
    for i in date:
        if i == '-':
            turtle.write("年",font=("Song typeface",20,"normal"))
            turtle.pencolor("DarkTurquoise")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Song typeface",20,"normal"))
            turtle.pencolor("PaleTurquoise")
            turtle.fd(40)
        elif i == '+':
            turtle.write("日",font=("Song typeface",20,"normal"))
            turtle.pencolor("PowderBlue")
            turtle.fd(40)
        elif i == '.':
            turtle.write("时",font=("Song typeface",20,"normal"))
            turtle.pencolor("Cyan")
            turtle.fd(40)
        elif i == '*':
            turtle.write("分",font=("Song typeface",20,"normal"))
            turtle.pencolor("LightYellow2")
            turtle.fd(40)
        elif i == '$':
            turtle.write("秒",font=("Song typeface",20,"normal"))
            turtle.fd(40)
        else:
            drawdigit(eval(i))
def main():
    turtle.setup(1520,790,0,0)
    turtle.penup()
    turtle.fd(-600)
    turtle.pensize(5)
    drawdate(time.strftime("%Y-%m=%d+%H.%M*%S$",time.localtime()))
    turtle.hideturtle()
    turtle.done()
main()

