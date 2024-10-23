

def char_freq(word):
    char_frequency = {}
    for char in word:
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1
    return char_frequency

def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    if char_freq(s) == char_freq(t):
        return True
    return False
    


s = "anagram"
t = "nagaram"
print(valid_anagram(s, t))