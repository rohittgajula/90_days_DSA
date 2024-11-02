

def first_palindromic_string(words):
    for word in words:
        if word != word[::-1]:
            continue
        else:
            return word
    return ""



words = ["abc","car","ada","racecar","cool"]
print(first_palindromic_string(words))