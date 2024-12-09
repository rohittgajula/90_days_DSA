

def constructTransformedArray(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        if nums[i] > 0:
            new_index = (i + nums[i]) % n
            result[i] = nums[new_index]
        elif nums[i] < 0:
            new_index = (i + nums[i] + n) % n
            result[i] = nums[new_index]
        else:
            result[i] = 0
    return result

nums = [3,-2,1,1]
print(constructTransformedArray(nums))