from collections import defaultdict


def most_frequent_word(text):
    
    words = text.lower().split(" ")
    
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    most_frequent = max(word_count, key=word_count.get) # word_count.get is a method of the dictionary that returns the value (the frequency) of a given word (key).
    return most_frequent
    

text = "apple banana apple orange apple banana"
print(most_frequent_word(text))

