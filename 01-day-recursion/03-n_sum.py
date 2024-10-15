



class Solution:
    def n_sum_with_recursion(self, n):
        if n == 0:              # base case
            return 0
        else:
            return self.n_sum_with_recursion(n-1) + n
        
    # time comp : O(n) - n recursive calls
    # space comp : O(n) - recursive call data is stored until base case
        

    def n_sum_without_recursion(self, n):
        result = 0
        for i in range(1,n+1):
            result += i
        return result
    # time comp : O(n) - n recursive calls
    # space comp : O(n)

n = 500
solution = Solution()
print(solution.n_sum_with_recursion(n))
print(solution.n_sum_without_recursion(n))

