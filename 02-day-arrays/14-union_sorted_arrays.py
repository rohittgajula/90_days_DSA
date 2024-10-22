

def union_sorted_array(nums1, nums2):
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
        else:           # nums1[i] == nums2[j]
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
    
    while i < len(nums1):
        if result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < len(nums2):
        if result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    
    return result


def union_array_using_set(nums1, nums2):
    s = set()
    union = []

    for item in nums1:
        s.add(item)
    for item in nums2:
        s.add(item)
    for num in s:
        union.append(num)
    return union

        
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 3, 3, 5, 6]
print(union_sorted_array(nums1, nums2))
print(union_array_using_set(nums1, nums2))

