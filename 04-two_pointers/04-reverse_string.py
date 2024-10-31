


def reverse_string(s):
    l = 0
    r = len(s)-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


s = ["h","e","l","l","o"]
print(reverse_string(s))