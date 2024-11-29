# two pointer

# using 2 pointer - r to scan through array & l to count unique place

# return len value
def remove_duplicates(nums):
    l = 0
    for r in range(1,len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
    return l + 1


nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))

