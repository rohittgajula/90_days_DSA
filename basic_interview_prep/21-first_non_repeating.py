# Find First Non-Repeated Character: Find the first non-repeated character in a string.


def non_repeating(s):
    hashMap = {}
    for char in s:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
    
    for key, value in hashMap.items():
        if value == 1:
            return key
    return None

s = "swisswxi"
print(non_repeating(s))