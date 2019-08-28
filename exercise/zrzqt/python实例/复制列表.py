#定义一个列表，并将该列表元素复制到另外一个列表上。
def clone_zrzqt(li1):
    li_copy = li1[:]
    return li_copy
li1 = [4,8,2,10,15,18]
li2 = clone_zrzqt(li1)
print('原始列表：',li1)
print('复制后列表：',li2)
#第二种 使用extend()方法
'''
def clone_zrzqt(li1): 
    li_copy = [] 
    li_copy.extend(li1) 
    return li_copy 
  
li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_zrzqt(li1) 
print("原始列表:", li1) 
print("复制后列表:", li2)
'''
#第三种 使用list()方法
'''
def clone_zrzqt(li1): 
    li_copy = list(li1) 
    return li_copy 
  
li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_zrzqt(li1) 
print("原始列表:", li1) 
print("复制后列表:", li2)
'''
