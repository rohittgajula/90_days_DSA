

# neetcode approach
def longest_subseting(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res


def substring_without_repeating(s):
    seen = {}
    l = 0
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            length = max(length, r - l + 1)
        seen[char] = r
    return length

s = "abcabcbb"
print(longest_subseting(s))
print(substring_without_repeating(s))