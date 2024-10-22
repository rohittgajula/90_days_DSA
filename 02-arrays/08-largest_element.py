

class Solution:
    def largest_element(self, arr):
        arr.sort()
        return arr[-1]
    
    def largest_loop(self, arr):
        largest_element = arr[0]
        for element in arr:
            if element > largest_element:
                largest_element = element
        return largest_element

solution = Solution()
arr = [1, 8, 7, 56, 90]
print(solution.largest_element(arr))
print(solution.largest_loop(arr))
