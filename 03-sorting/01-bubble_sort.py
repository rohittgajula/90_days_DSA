# Bubble sort is a sorting algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)- i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


nums = [2,8,5,3,9,4,1]
print(bubble_sort(nums))




# temp = arr[i]
# arr[i] = arr[min_index]
# arr[min_index] = temp