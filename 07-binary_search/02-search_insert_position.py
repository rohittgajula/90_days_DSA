

def search_insert_position(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        middle = (left+right)//2
        if target == nums[middle]:
            return middle
        if target < nums[middle]:
            right = middle-1
        else:
            left = middle+1
    return left                         # here left is suitable instead of right (follow neetcode video)


nums = [1,3]
target = 2
print(search_insert_position(nums, target))