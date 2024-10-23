# Given a string s consisting of words and spaces, return the length of the last word in the string. 

def length_of_last_word_with_spaces(s):
    count = 0
    i = len(s) - 1

    while i >= 0 and s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        count += 1
        i -= 1
    return count


# this works fine if there are no spaces in the end.
def length_of_last_word(s):
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            count += 1
        else:
            return count
        
def solution_using_for_loop(s):
    count = 0
    found_word = False

    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            count += 1
            found_word = True
        elif found_word:
            break
    return count


s = "Hello World"
print(length_of_last_word_with_spaces(s))
print(length_of_last_word(s))
print(solution_using_for_loop(s))
