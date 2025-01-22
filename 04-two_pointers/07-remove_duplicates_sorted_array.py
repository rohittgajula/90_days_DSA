
# the array is sorted. we are moving left pointer one step ahead whenever we see a new number and ignoring all the duplicates.


def remove_duplicates(nums):
    l = 0
    for r in range(1, len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
    return l+1


def brute_force(nums):
    seen = set()
    unique_nums = [nums[0]]
    for i in range(1, len(nums)):
        if (nums[i] != nums[i-1]) and (nums[i] not in seen):
            unique_nums.append(nums[i])
            seen.add(nums[i])
    return unique_nums

nums = [0,0,1,1,1,2,2,3,3,4]
# print(remove_duplicates(nums))
print(brute_force(nums))

