# Check if two strings are anagrams


def count_occurance(s):
    
    hashMap = {}
    for w in s:
        if w not in hashMap:
            hashMap[w] = 1
        else:
            hashMap[w] += 1
    return hashMap


s = "hai rohit how are you"
print(count_occurance(s))