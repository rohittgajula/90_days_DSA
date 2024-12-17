# Remove Duplicates: Remove duplicate characters from a string.


def remove_duplicates(s):
    res = []
    for char in s:
        if char not in res:
            res.append(char)
    return "".join(res)


s = "abacadae"
print(remove_duplicates(s))