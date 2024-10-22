


def linear_search(nums, k):
    
    for i in range(len(nums)):
        if nums[i] == k:
            return True
    return False


nums = [1, 2, 3, 4, 6]
k = 6
print(linear_search(nums, k))