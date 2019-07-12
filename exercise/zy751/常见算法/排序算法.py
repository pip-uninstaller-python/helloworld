def hebing(list):#合并排序
    if len(list)<=1:
        return list
    middle=len(list)//2#取中间值，将列表分为左边和右边
    lef=list[:middle]
    rig=list[middle:]
    lef=hebing(lef)#将俩边继续细分
    rig=hebing(rig)
    return sort(lef,rig)#返回的值为排好序的列表
def sort(list1,list2):
    list=[]#创建一个控列表
    a=b=0
    while a<len(list1) and b<len(list2):#当有一个列表不为空时就可以继续笔记,比过的就不必了
        if list1[a]<list2[b]:
            list.append(list1[a])
            a+=1
        else:
            list.append(list2[b])
            b+=1
    else:#比完时必有一个列表还有未比过的，将未比的直接加入列表
        if a==len(list1):
            for i in list2[b:]:
                list.append(i)
        else:
            for i in list1[a:]:
                list.append(i)
    return list
list1=[2,5,8,5,2,22,33]
a=hebing(list1)
print(a)
def mp(list):#冒泡
    if len(list)<=1:
        return list
    for i in range(len(list)-1,0,-1):#第一个元素要比较len-1次，第二个len-2.。。。
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
print(mp(list1))
def xe(list):#希尔
    gap=len(list)//2#找到中点
    while gap>0:
        for i in range(gap,len(list)):#找右边的元素
            temp=list[i]#当前元素值
            j=i#当前元素位置
            while j>=gap and a[j-gap]>temp:#通过比较左右俩边相对应的位置
                list[j]=list[j-gap]
                j=j-gap
            a[j]=temp
        gap=gap//2
    return list
print(xe(list1))
def xz(list):
    for i in range(len(list)):#本算法思想 ：从第一个元素开始 先将本位制元素定为最小，通过与后面的比较换位，使本位置元素最小，依次下去，排序完成
        min_i=i
        for j in range(i+1,len(list)):
            while list[min_i]>list[j]:
                list[min_i],list[j]=list[j],list[min_i]
    return list
print(xz(list1))
def cr(list):#插入算法
    for i in range(1,len(list)):#算法思想：从第一个位置开始跟后面元素比较，最小的放第一位，第二位，实现排序
        j=i-1
        net=a[i]
        while net<a[j] and j>=0:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=net
    return list
print(cr(list1))