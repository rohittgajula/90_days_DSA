

def bubble_sort(nums):
    
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [4,2,7,9,5,6]
print(bubble_sort(nums))

