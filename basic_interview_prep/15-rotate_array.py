# Rotate an array by k positions.


def rotate_array(nums, k):
    n = len(nums)
    rotated = [0] * n
    for i in range(n):
        correct_index = (i + k) % n
        rotated[correct_index] = nums[i]
    return rotated


nums = [1,2,3,4,5]
k = 2
print(rotate_array(nums, k))