


def find_missing_range(nums, lower, upper):
    
    n = len(nums)
    missing_range = []

    if n == 0:
        return [[lower, upper]]
    
    if lower < nums[0]:
        missing_range.append([lower, nums[0]-1])

    for i in range(n-1):
        if nums[i+1] - nums[i] <= 1:
            continue
        missing_range.append([nums[i]+1, nums[i+1]-1])
    
    if nums[-1] < upper:
        missing_range.append([nums[-1]+1, upper])

    return missing_range



nums = [0,1,3,50,75]
lower = 0
upper = 99
print(find_missing_range(nums, lower, upper))