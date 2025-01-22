


def remove_duplicates(nums):
    l = 0
    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
    return nums[:l+1]


def remove_dup(nums):
    seen = set()
    unique_nums = [nums[0]]
    for i in range(len(nums)):
        if (nums[i] != unique_nums[-1]) and (nums[i] not in seen):
            unique_nums.append(nums[i])
            seen.add(nums[i])
    return unique_nums

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
print(remove_dup(nums))