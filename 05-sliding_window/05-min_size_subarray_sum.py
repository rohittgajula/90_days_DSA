# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


def min_size_subarray_sum(nums, target):
    min_length = float('inf')
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right-left+1)
            current_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0



nums = [2,3,1,2,4,3]
target = 7
print(min_size_subarray_sum(nums, target))







# if target in nums:
#         return "1"
    
#     l = 0
#     r = 1
#     subarray_sum = sum(nums[:r])
#     subarray_length = l - r + 1

#     while r < len(nums):
#         if subarray_sum >= target:
#             return subarray_length
#         elif subarray_sum < target:
#             subarray_sum += nums[r + 1]
#             r += 1
#             subarray_length = l - r + 1
#         elif subarray_sum > target:
#             subarray_sum -= nums[l - 1]
#             l += 1
#             subarray_length = l - r + 1
#     return subarray_length