# https://youtu.be/kMzJy9es7Hc


# this is my solution
def findPeakElement(nums):
    def binarySearch(left, right):
        if left == right:
            return left

        mid = (left + right) // 2
        if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
            return mid
        
        if (mid < len(nums) - 1) and (nums[mid] < nums[mid + 1]):
            return binarySearch(mid + 1, right)
        
        return binarySearch(left, mid)
    
    return binarySearch(0, len(nums) - 1)

# THIS IS NOT WORKING FOR [4,3,2,1] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# neetcode solution
def find_peak(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - 1) // 2)
        # check if left neighbor is greater
        if mid > 0 and nums[mid] < nums[mid - 1]:
            r = mid - 1
        # check right neighbor is greater
        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            return mid



# from submitted solutions
# if the right element to mid is greater it is sure that peak element is towards right.
def find_peak_element(nums):
    if len(nums) == 1:
        return 0
    
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


nums = [4,3,2,1]
print(findPeakElement(nums))
print(find_peak(nums))
print(find_peak_element(nums))

