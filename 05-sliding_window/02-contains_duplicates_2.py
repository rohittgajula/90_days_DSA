

def contains_duplicates(nums, k):
    
    hashMap = {}
    for i in range(len(nums)):
        if nums[i] in hashMap and abs(i - hashMap[nums[i]]) <= k:
            return True
        hashMap[nums[i]] = i
    return False

nums = [1,2,3,1]
k = 3
print(contains_duplicates(nums, k))

