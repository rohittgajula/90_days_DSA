# Write a function to check if a given string is a palindrome.


def isPalindrome(s):
    l = 0
    r = len(s)-1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


s = "race a car"
print(isPalindrome(s))

