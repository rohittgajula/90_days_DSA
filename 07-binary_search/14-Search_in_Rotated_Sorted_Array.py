


def search_rotated_sorted_array(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle
        # check left sorted array
        if nums[left] <= nums[middle]:
            if target > nums[middle] or target < nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        # check right sorted array
        else:
            if target < nums[middle] or target > nums[right]:
                right = middle - 1
            else:
                left = middle - 1
    return -1



nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated_sorted_array(nums, target))