# Find the maximum and minimum elements in an array.


def max_min(nums):
    max_element = nums[0]
    min_element = nums[0]

    for num in nums:
        if num > max_element:
            max_element = num

    for num in nums:
        if num < min_element:
            min_element = num
    
    return max_element, min_element



nums = [2,3,6,4,9,1]
print(max_min(nums))