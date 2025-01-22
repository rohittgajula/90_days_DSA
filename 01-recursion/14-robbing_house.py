



# tapping rain water

def BruteForce(nums, index=0):
    if index >= len(nums):
        return 0
    # [2,1,1,2]
    rob_current = nums[index] + BruteForce(nums, index+2)
    skip_current = BruteForce(nums, index+1)

    print(f'rob current : {rob_current}')
    print(f'skip current : {skip_current}')
    return max(rob_current, skip_current)
    

def OptimalDP(nums):
    rob1 = 0
    rob2 = 0

    # [rob1, rob2, n, n+1, ....]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


nums = [1,2,3,1]
print(BruteForce(nums))
# print(OptimalDP(nums))