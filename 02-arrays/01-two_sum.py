# two pointer


class Solution:
    # using two pointers - O(n^2)
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
    # dict - O(n)
    def two_sum_hashmap(self, nums, target):
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return None
    
    # binary search logic - O(1)
    def two_sum_using_while(self, nums, target):
        left = 0
        right = len(nums)-1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1


nums = [2,7,11,15]
target = 26
solution = Solution()
print(solution.two_sum(nums, target))
print(solution.two_sum_hashmap(nums, target))
print(solution.two_sum_using_while(nums, target))