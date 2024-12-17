# Remove duplicates from a list.

def remove_duplicates(nums):
    uniques_num = list(set(nums))
    return uniques_num

def remove_duplicates_2(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

nums = [3,4,1,2,6,7,4,3,1,1]
print(remove_duplicates(nums))
print(remove_duplicates_2(nums))

