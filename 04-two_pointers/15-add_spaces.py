


def addSpaces(s, spaces):
    result = []
    i = 0

    for index in spaces:
        portion = s[i:index]
        result.append(portion)
        i = index
    result.append(s[spaces[-1]:])
    return " ".join(result)


# two pointers
def add_spaces(s, spaces):
    i = 0
    j = 0
    res = []

    while i < len(s) and j < len(spaces):
        if i < spaces[j]:
            res.append(s[i])
            i += 1
        else:
            res.append(" ")
            j += 1
    
    if i < len(s):
        res.append(s[i:])

    return "".join(res)

s = "HaiRohitGajula"
spaces = [3,8]
print(addSpaces(s, spaces))
print(add_spaces(s, spaces))


