# 153 - Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:


def find_min_rotated_sorted_arr(nums):
    left = 0
    right = len(nums) - 1
    res = nums[0]

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        middle = (left + right) // 2
        res = min(res, nums[middle])
        if nums[middle] >= nums[left]:
            left = middle + 1
        else:
            right = middle - 1
    return res

# brute force
def findMin(nums):
    pass


nums = [3,4,5,1,2]
print(find_min_rotated_sorted_arr(nums))