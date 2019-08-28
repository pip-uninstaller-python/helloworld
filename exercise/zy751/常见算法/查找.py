def find(list,data):
    list=sorted(list)
    for i in range(len(list)):
        if list[i]==data:
            print(i)
            return i
    print('所找数据不在列表内')
def er_find(list,data):
    list=sorted(list)
    left,right=0,len(list)-1
    while left<right:
        middle=(left+right)//2
        if list[middle]==data:
            print(middle)
            return middle
        elif list[middle]<data:
            left=middle
        else:
            right=middle
    else:
        print('不在')
list=[29,4,5,342,24]
list1=sorted(list)
print(list1.index(29))
find(list,28)
find(list,29)
er_find(list,2)
er_find(list,29)
