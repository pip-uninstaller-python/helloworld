count = 0
def hanoi(n,x,y,z):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,x,y))
        count += 1
    else:
        hanoi(n-1,x,z,y)
        print("{}:{}->{}".format(n,x,y))
        count += 1
        hanoi(n-1,z,y,x)
hanoi(3,"A","C","B")
print(count)