'''
选择排序是一种简单直观的排序算法。
它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
'''
import sys 
A = [64, 25, 12, 22, 11] 
  
for i in range(len(A)): 
      
   
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
                
    A[i], A[min_idx] = A[min_idx], A[i] 
  
print ("排序后的数组：") 
for i in range(len(A)): 
    print("%d" %A[i]),
#第二种可选择升序或降序
#待排序数组arr，排序方式order>0升序，order<0降序
'''
def selectSort(arr,order):
    rborder = len(arr)
    for i in range(0,rborder):
        p = i
        j = i+1
        while(j<rborder):
            if((arr[p]>arr[j]) and (int(order)>0)) or ((arr[p]<arr[j]) and (int(order)<0)):
                p = j
            j += 1
        arr[i], arr[p] = arr[p], arr[i]
        i += 1
    return arr

A = [64, 25, 12, 22, 11] 
print(selectSort(A, -1))
print(selectSort(A, 1))
'''
