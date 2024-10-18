


class Solution:
    # using two pointers
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
    def two_sum_hashmap(self, nums, target):
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
            print(hashMap)
        return None


nums = [2,7,11,15]
target = 26
solution = Solution()
print(solution.two_sum(nums, target))
print(solution.two_sum_hashmap(nums, target))