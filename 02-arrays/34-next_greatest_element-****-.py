

def next_greatest_element(nums1, nums2):
    nums1idx = {}
    res = [-1] * len(nums1)

    for i, n in enumerate(nums1):
        if n not in nums1idx:
            nums1idx[n] = i
    
    # nums1 = [4,1,2] nums2 = [1,3,4,2]
    for i in range(len(nums2)):
        if nums2[i] not in nums1idx:
            continue
        for j in range(i+1, len(nums2)):
            if nums2[j] > nums2[i]:
                idx = nums1idx[nums2[i]]
                res[idx] = nums2[j]
                break
    return res


def next_greatest(nums1, nums2):

    stack = []
    ngr = {}

    # Iterate through nums2 in reverse order
    for i in range(len(nums2) - 1, -1, -1):
        current = nums2[i]
        # Maintain a stack of next greater elements
        while stack and stack[-1] <= current:
            stack.pop()
        # If the stack is empty, there's no greater element
        if not stack:
            ngr[current] = -1
        else:
            ngr[current] = stack[-1]
        stack.append(current)

    # Build the result for nums1 using the map
    ans = []
    for num in nums1:
        ans.append(ngr[num])

    return ans


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greatest_element(nums1, nums2))
print(next_greatest(nums1, nums2))