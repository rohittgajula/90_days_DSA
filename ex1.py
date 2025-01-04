
class TwoSum:
    # O(n^2)
    def solution1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
    
    # O(n) - dict
    def solution2(self, nums, target):
        hashMap = {}
        for i, n in enumerate(nums):
            hashMap[n] = i
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in hashMap:
                return [hashMap[diff], j]
        return None
    
    # O(1) - binary search logic - two pointers
    def solution3(self, nums, target):
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
        return None


nums = [2,7,11,15]
target = 18
sol = TwoSum()
print(sol.solution1(nums, target))
print(sol.solution2(nums, target))
print(sol.solution3(nums, target))


