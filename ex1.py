

def robber(nums):
    prod1 = 0
    prod2 = 0
    for i in range(0, len(nums), 2):
        prod1 += nums[i]
    
    for j in range(1, len(nums), 2):
        prod2 += nums[j]

    return max(prod1, prod2)


nums = [2,1,1,2]
print(robber(nums))