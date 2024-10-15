

def powerset(arr):
    
    if len(arr) == 0:
        return [[]]
    else:
        allSubsets = []
        for subset in powerset(arr[1:]):
            allSubsets += [subset]
            allSubsets += [[arr[0]] + subset]
        return allSubsets



arr = [1,2]
print(powerset(arr))



