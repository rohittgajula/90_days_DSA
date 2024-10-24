from collections import defaultdict


def majority_element(nums):
    hashSet = {}
    for i in nums:
        if i not in hashSet:
            hashSet[i] = 1
        else:
            hashSet[i] += 1
    for num, count in hashSet.items():
        if count > len(nums) // 2:
            return num


nums = [3,2,3]
print(majority_element(nums))

