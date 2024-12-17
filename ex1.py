


def mergeAlternately(word1, word2):
    i = 0
    j = 0
    res = []
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])
    return "".join(res)


word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))