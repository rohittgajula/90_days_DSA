def sum_of_two(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)-1):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

nums = [2,7,11,15]
target = 9
print(sum_of_two(nums, target))