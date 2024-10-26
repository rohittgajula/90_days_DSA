# Selection sort is a sorting algorithm that divides the list into a sorted and an unsorted part. It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted portion and swaps it with the first unsorted element, growing the sorted part by one element in each iteration.


def selection_sort(nums):
    
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]
        print(nums)
    return nums

nums = [2,8,5,3,9,4,1]
print(selection_sort(nums))

