#给定一个字典，然后计算它们所有数字值的和。
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum
dict = {'a':100,'b':200,'c':300}
print('Sum:',returnSum(dict))
