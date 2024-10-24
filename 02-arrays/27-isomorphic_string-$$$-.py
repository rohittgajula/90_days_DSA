# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


def isomorphic_string_without_inbuilt_function(s, t):
    if len(s) != len(t):
        return False
    else:
        hashMap = {}

        for i in range(len(s)):
            if s[i] not in hashMap:
                if t[i] not in hashMap.values():
                    hashMap[s[i]] = t[i]
                else:
                    return False
            else:
                if hashMap[s[i]] != t[i]:
                    return False
    return True

def isomorphic_string(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s
    
    return True

s = "egg"
t = "add"
print(isomorphic_string_without_inbuilt_function(s, t))
print(isomorphic_string(s, t))