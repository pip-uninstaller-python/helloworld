#定义一个数字列表，并计算列表元素之积。
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplyList(list1))
print(multiplyList(list2))
