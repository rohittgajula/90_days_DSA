# two pointer

def remove_element(nums, val):
    
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


nums = [3,2,2,3]
val = 2
print(remove_element(nums, val))