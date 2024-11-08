


def binary_search(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        middle = (l+r)//2
        if target == nums[middle]:
            return middle
        elif (target > nums[middle]):
            l = middle + 1
        else:
            r = middle - 1
    return -1


nums = [-1,0,3,5,9,12]
target = 12
print(binary_search(nums, target))

