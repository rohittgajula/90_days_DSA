

# l, r pointers start from index 0, if that pointer is not 0 then then we swap with the left pointer, if there is a zero move the right pointer by one step in loop.

def move_zeros(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l],  nums[r] = nums[r], nums[l]
            l += 1
    return nums

def brute_force(nums):
    
    result = [0] * len(nums)
    count = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            result[count] = nums[i]
            count += 1
    return result


nums = [0,1,0,3,12]
print(move_zeros(nums))
print(brute_force(nums))
