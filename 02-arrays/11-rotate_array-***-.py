
def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    l = 0
    r = n-1
    # rotate the whole array
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    # rotate first part of array till k
    l = 0
    r = k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    # rotate 2nd part of array from k to n
    l = k
    r = n-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    return nums


def rotate(nums, k):
    n = len(nums)
    rotate = [0] * n
    for i in range(n):
        correct_index = (i + k) % n
        rotate[correct_index] = nums[i]
    return rotate


def rotateArray(nums, k):
    n = len(nums)
    for _ in range(k):
        last = nums[-1]
        for i in range(n-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = last
    return nums


nums = [1,2,3,4,5]
k = 2
print(rotate_array(nums[:], k))     # Pass a copy of nums
print(rotate(nums[:], k))
print(rotateArray(nums[:], k))      # Pass a copy of nums