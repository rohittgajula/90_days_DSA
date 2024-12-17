# Given an array, find a pair of numbers that add up to a given target.



def two_sum(nums, target):
    
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def using_hashmap(nums, target):
    hashMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
    return None



nums = [4,2,7,9,5,6]
target = 11
print(two_sum(nums, target))