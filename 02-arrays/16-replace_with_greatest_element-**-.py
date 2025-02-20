# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.


def replace_element(nums):
    rightMax = -1
    for i in range(len(nums)-1, -1, -1):
        newMax = max(rightMax, nums[i])
        nums[i] = rightMax
        rightMax = newMax
    return nums


def replaceElement(nums):
    for i in range(len(nums)):
        if i == len(nums)-1:
            nums[i] = -1
        else:
            nums[i] = max(nums[i+1:])
    return nums


nums = [17,18,5,4,6,1]
print(replace_element(nums.copy()))
print(replaceElement(nums.copy()))

