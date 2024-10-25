



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

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(nums, k))