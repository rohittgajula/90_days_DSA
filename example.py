


def find_sim(nums1, nums2):
    
    common_elem = set()

    for elem1 in nums1:
        for elem2 in nums2:
            if elem1 == elem2:
                common_elem.add(elem1)
    return common_elem


nums1 = [3,7,1,5,9,15,21]
nums2 = [3,10,16,5,3,27]
print(find_sim(nums1, nums2))


