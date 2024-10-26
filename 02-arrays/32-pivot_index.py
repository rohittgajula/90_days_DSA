

def pivot_index(nums):
    
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1



nums = [1,7,3,6,5,6]
print(pivot_index(nums))
