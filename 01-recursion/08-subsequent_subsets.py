


class Solution:
    def powerset(self, arr):
        
        if len(arr) == 0:
            return [[]]
        else:
            allSubset = []
            for subset in self.powerset(arr[1:]):
                allSubset += [subset]
                allSubset += [[arr[0]] + subset]
            return allSubset
        
    def subsets_without_recursion(self, arr):
        subsets = [[]]

        for element in arr:
            new_subsets = []

            for subset in subsets:
                new_subset = subset + [element]
                new_subsets.append(new_subset)
            
            subsets.extend(new_subsets)

        return subsets

solution = Solution()
arr = [1,2]
# print(solution.powerset(arr))
print(solution.subsets_without_recursion(arr))

