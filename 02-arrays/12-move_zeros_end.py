



def move_zeros_end(nums):
    
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums

def move_zeros_BF(nums):
    result = [0] * len(nums)
    index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            result[index] = nums[i]
            index += 1
    return result


nums = [0,1,0,3,12]
print(move_zeros_end(nums))
print(move_zeros_BF(nums))
