


class Solution:
    def two_power_recursion(self, n):
        if n == 0:
            return 1
        else:
            return self.two_power_recursion(n-1) * 2
        
    def two_power_without_recursion(self, n):
        result = 1
        for i in range(n):
            result = result * 2
        return result

n = 5
solution = Solution()
print(solution.two_power_recursion(n))
print(solution.two_power_without_recursion(n))

