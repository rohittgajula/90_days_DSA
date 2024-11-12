# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.
# l + ((r - 1) // 2) - another way of finding middle


def single_element(nums):
    left = 0
    right = len(nums)

    while left < right:
        middle = (left + right) // 2
        if ((middle - 1 < 0 or nums[middle - 1] != nums[middle]) and (middle + 1 == len(nums) or nums[middle] != nums[middle + 1])):
            return nums[middle]
        
        leftSide = (middle - 1) if nums[middle - 1] == nums[middle] else middle
        if (leftSide % 2) != 0:
            right = middle - 1
        else:
            left = middle + 1


nums = [1,1,2,3,3,4,4,8,8]
print(single_element(nums))


