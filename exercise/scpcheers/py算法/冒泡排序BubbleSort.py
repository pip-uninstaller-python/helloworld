arr = [7, 4, 3, 67, 34, 1, 8]

# py冒泡排序
# 第一个与往后的其它数值比大小，满足条件替换，
# 然后依次往后循环，直到循环完所有的数值。
# 时间复杂度：
def bubble_sort(arr):
    length = len(arr)  # 数组长度
    for y in range(0, length-1):
        for x in range(0, length-1-y):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]

bubble_sort(arr)
print(arr)