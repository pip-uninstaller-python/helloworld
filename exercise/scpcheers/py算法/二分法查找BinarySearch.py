# 二分法查找
import time


def binary_search(li, val):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] > val:
            high = mid - 1
        elif li[mid] < val:
            low = mid + 1
        else:
            return mid
    else:
        return None


def linear_search(li, val):
    try:
        i = li.index(val)
        return i
    except:
        return None


if __name__ == '__main__':
    start = time.time()
    li = list(range(0, 10000000))
    print(binary_search(li, 8880000))
    end = time.time()
    times = end - start
    print("用时：" + str(times))

