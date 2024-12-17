# Check if two strings are anagrams


def anagram(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def anagram_1(s):
    return s == s[::-1]

s = "tenet"
print(anagram(s))
print(anagram_1(s))