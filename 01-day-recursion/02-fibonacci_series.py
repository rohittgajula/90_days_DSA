

# Fibonacchi series -> 0,1,1,2,3,5,8,13......
# Sum of two preceding once.


class Solution:
    def fibonacchi_without_recursion(self, n):
        
        result = [0,1]
        for i in range(2, n):
            result.append(result[-1] + result[-2])
        return result
    
    # time comp : O(n) - n recursive calls
    # space comp : O(n) - list stores n elements

    def fibonacchi_recursion(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacchi_recursion(n-1) + self.fibonacchi_recursion(n-2)
        
    # Time complexity: O(2^n) - exponential due to overlapping subproblems
    # Space complexity: O(n) - recursion depth is n


solution = Solution()
n = 5
print(solution.fibonacchi_without_recursion(n))
print([solution.fibonacchi_recursion(i) for i in range(n)])

