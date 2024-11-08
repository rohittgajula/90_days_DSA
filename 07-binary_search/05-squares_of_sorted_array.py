# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# binary search - O(n)
def square_sorted_array(nums):
    n = len(nums)
    left = 0
    right = n - 1
    res = [0] * n
    pos = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            res[pos] = left_square
            left += 1
        else:
            res[pos] = right_square
            right -= 1
        pos -= 1
    return res



# brute force approach - O(n)
def squares_sorted_array(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    nums.sort()
    return nums


nums = [-4,-1,0,3,10]
print(square_sorted_array(nums))
print(squares_sorted_array(nums))