

# A function which calls itself is called recursive

#      (recursive case)
# 5! = 5*4! -> 4*3! -> 3*2! -> 2*1! -> 1*1(base case)

class Solution:
    def factorial(self, n):
        if n == 0:              # base case
            return 1
        else:
            return n * self.factorial(n-1)
    # time comp : O(n) - n recursive calls
    # space comp : O(n) - each recursive call is stored in stack until base case
        
    def without_recursion(self, n):
        result = 1
        for i in range(2, n + 1):           # range (start, stop-1) -> n=5 -> (2, 4+1)
            result *= i
        return result
    # time comp : O(n) - n recursive calls
    # space comp : O(1) - only uses few variables regardless of size ie. result, i

solution = Solution()
n = 5
print(solution.factorial(n))
print(solution.without_recursion(n))

