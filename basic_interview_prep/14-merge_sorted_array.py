# Merge two sorted arrays into a single sorted array.


def merge_array(nums1, nums2):
    i = 0
    j = 0
    merged_array = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i += 1
        else:
            merged_array.append(nums2[j])
            j += 1
    
    while i < len(nums1):
        merged_array.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged_array.append(nums2[j])
        j += 1
    
    return merged_array



nums1 = [1,3,5,7]
nums2 = [2,4,6,8]
print(merge_array(nums1, nums2))