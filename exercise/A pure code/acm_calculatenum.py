
'''
给定一个整数数组nums和一个目标值target,请你在该数组中找出
和为目标值得那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用
这个数组中同样的元素。
'''


def addlit(nums, target):
    for idx, val in enumerate(nums):
        temp = target - val
        for jdx in range(idx + 1, len(nums)):
            if temp == nums[jdx]:
                return (idx, jdx), (nums[idx], nums[jdx])
    return 0, 0


t = addlit([2, 5, 8, 3], 8)
print(t)
