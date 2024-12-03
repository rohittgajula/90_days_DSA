


def merge_list(list1, list2):
    i = 0
    j = 0
    res = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    
    if i < len(list1):
        res.extend(list1[i:])
    elif j < len(list2):
        res.extend(list2[j:])

    return res


list1 = [1,3,4,5,9]
list2 = [2,7,8]
print(merge_list(list1, list2))