

def check_equivalent(word1, word2):
    
    word1 = "".join(word1)
    word2 = "".join(word2)

    if word1 == word2:
        return True
    else:
        return False


word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(check_equivalent(word1, word2))
