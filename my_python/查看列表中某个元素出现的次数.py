#方法一
from collections import Counter
a = [1,2,2,2,2,3,3,3,4,4,4,4]
b= Counter(a)
print(b)


#方法二
mylist = [1,2,2,2,2,3,3,3,4,4,4,4]
myset = set(mylist)  #myset是另外一个列表，里面的内容是mylist里面的无重复项
for item in myset:
  print("the %d has found %d" %(item,mylist.count(item)))


#方法三
List=[1,2,2,2,2,3,3,3,4,4,4,4]
a = {}
for i in List:
	a[i] = List.count(i)
print (a)


# 寻找名字中带有两个e的人的名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# 不用推导式
result = []
for first in names:
    for name in first:
        if name.count("e") >= 2:
            result.append(name)
print(result)



# 推导式
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
gen = (name for first in names for name in first if name.count('e') >= 2)
for i in gen:
    print(i)