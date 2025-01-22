# two pointer

# using 2 pointer - r to scan through array & l to count unique place

# return len value
# O(n)
def remove_duplicates(nums):
    l = 0
    for r in range(1,len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
    return l + 1            # if we want to return arr = nums[:l+1]

# brute force - O(n*m)
def remove_duplicates_BF(nums):
    result = []
    for i in range(len(nums)):
        for j in range(len(result)):
            if nums[i] == result[j]:
                break
        else:
            result.append(nums[i])
    return result


nums = [0,0,1,1,2,2]
print(remove_duplicates(nums))
print(remove_duplicates_BF(nums))
