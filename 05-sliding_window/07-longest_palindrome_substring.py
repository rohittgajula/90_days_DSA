
def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def find_longest_palindrome(s):
    l = 0
    r = 0
    longest_palindrome = ""

    while l < len(s):
        if r < len(s) and is_palindrome(s, l, r):
            current_substring = s[l:r+1]
            if len(current_substring) > len(longest_palindrome):
                longest_palindrome = current_substring
        
        if r < len(s):
            r += 1
        else:
            l += 1
            r = l
    return longest_palindrome

s = "tenet"
print(find_longest_palindrome(s))