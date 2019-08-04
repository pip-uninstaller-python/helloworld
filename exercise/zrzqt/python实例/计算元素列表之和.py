#定义一个数字列表，并计算列表元素之和
total = 0
list1 = [11,5,17,18,23]
for ele in range(0,len(list1)):
    total = total + list1[ele]
print('列表元素之和为:',total)
#第二种 使用while()循环
'''
total = 0
ele = 0
  
list1 = [11, 5, 17, 18, 23]  
  
while(ele < len(list1)): 
    total = total + list1[ele] 
    ele += 1
      
print("列表元素之和为: ", total)
'''
#第三种 使用递归
'''
list1 = [11, 5, 17, 18, 23] 

def sumOfList(list, size): 
   if (size == 0): 
     return 0
   else: 
     return list[size - 1] + sumOfList(list, size - 1) 
      
total = sumOfList(list1, len(list1)) 

print("列表元素之和为: ", total)
'''
