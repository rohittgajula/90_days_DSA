


class Solution:
    def second_largest(self, arr):
        largest = arr[0]
        second_largest = arr[1]

        for element in arr:
            if element > largest:
                largest = element
        for element in arr:
            if element != largest and element > second_largest:
                second_largest = element
        return second_largest
    
    def second_largest2(self, arr):
        largest = arr[0]
        second_largest = arr[0]
        
        for element in arr:
            if element > largest:
                largest = element
        for element in arr:
            if element != largest and element > second_largest:
                second_largest = element
        return second_largest


solution = Solution()
arr = [12, 35, 1, 10, 34, 1]
print(solution.second_largest(arr))
print(solution.second_largest2(arr))