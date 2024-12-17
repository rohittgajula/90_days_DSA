# Find the second largest element in an array.



def second_largest(nums):
    largest_num = nums[0]
    second_largest = nums[0]

    for num in nums:
        if num > largest_num:
            largest_num = num
    for num in nums:
        if num != second_largest and num < second_largest:
            second_largest = num

    return largest_num, second_largest


nums = [4,2,7,9,5,6]
print(second_largest(nums))

