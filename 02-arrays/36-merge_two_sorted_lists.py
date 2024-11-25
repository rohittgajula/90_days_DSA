

# this is merging two array/list
def merge_sorted_list(nums1, nums2):
    merged_list = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i += 1
        else:
            merged_list.append(nums2[j])
            j += 1
    while i < len(nums1):               # check if any elements are leftover in nums1
        merged_list.append(nums1[i])
        i += 1
    while j < len(nums2):               # check if any elements are leftover in nums2
        merged_list.append(nums2[j])
        j += 1
    return merged_list

nums1 = [1,2,4]
nums2 = [1,3,4]
print(merge_sorted_list(nums1, nums2))