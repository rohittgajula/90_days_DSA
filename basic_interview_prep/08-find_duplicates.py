# Find all duplicate elements in a list.

def find_duplicates(nums):
    duplicates = {}
    hashMap = {}
    for num in nums:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1

    for key, value in hashMap.items():
        if value > 1:
            duplicates[key] = value
    return duplicates


nums = [3,4,1,2,6,7,4,3,1,1]
print(find_duplicates(nums))