


class Solution:
    def reverse_array(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        else:
            arr[0], arr[-1] = arr[-1], arr[0]
            self.reverse_array(arr[1:-1])
            return arr
        
    def reverse_array(self, arr):
        return arr[::-1]
        

arr = [1,2,3,4,5]
solution = Solution()
print(solution.reverse_array(arr))
print(solution.reverse_array(arr))

