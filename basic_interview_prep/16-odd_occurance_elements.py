# Find the element that occurs an odd number of times in an array.



def odd_occurance(nums):
    
    hashMap = {}
    res = []
    for num in nums:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1
    
    for key, value in hashMap.items():
        if value % 2 != 0:
            res.append(key)
    return res


nums = [4, 3, 4, 3, 4, 4, 4, 7]
print(odd_occurance(nums))