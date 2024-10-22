# two pointer


def merge_sorted_array(nums1, m, nums2, n):
    
    i = m - 1  # Pointer for nums1
    j = n - 1  # Pointer for nums2
    k = m + n - 1  # Pointer for the merged array
    
    # Merge from the back
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # If there are remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    # No need to check for remaining nums1 elements, they are already in place

    return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge_sorted_array(nums1, m, nums2, n))