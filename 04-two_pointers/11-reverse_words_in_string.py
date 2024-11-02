

def reverse_words(words):
    
    split_words = words.split(" ")
    res = []
    
    for word in split_words:
        reverse_word = word[::-1]
        res.append(reverse_word)
    
    return " ".join(res)


words = "Let's take LeetCode contest"
print(reverse_words(words))