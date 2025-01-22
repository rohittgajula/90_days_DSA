# two pointer

# optimal solution
def remove_element(nums, val):
    
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count                    # nums[:count]

# brute force
def remove_element_BF(nums, val):
    result = []
    for i in range(len(nums)):
        if nums[i] != val:
            result.append(nums[i])
    return result

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(nums, val))
print(remove_element_BF(nums, val))
