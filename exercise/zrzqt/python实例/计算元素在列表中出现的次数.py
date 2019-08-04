#定义一个列表，并计算某个元素在列表中出现的次数。
def countX(lst,x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
lst = [8,6,8,10,8,20,10,8,8]
x = 8
print(countX(lst,x))
#第二种 使用count()方法
'''
def countX(lst, x): 
    return lst.count(x) 
  
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
x = 8
print(countX(lst, x))
'''
