# exclusive, inclusive


# this works with everything
def valid_palindrome(s):
    l = 0
    r = len(s)-1

    while l < r:
        if s[l] != s[r]:
            skipL = s[l+1: r+1]     # In a slice like s[start:end], the start index is inclusive, meaning it starts the slice at the character at start.
            skipR = s[l: r]         # here r is exclusive ie. it stops the slice right before the character at end
            return (skipL == skipL[::-1] or
                    skipR == skipR[::-1])
        l += 1
        r -= 1
    return True


# this works for other solutions not for abc
def palindrome(s):
    l = 0
    r = len(s)-1
    count = 0

    while l < r:
        if s[l] != s[r]:
            count += 1
            if count > 1:
                return False
        l += 1
        r -= 1
    return True

s = "abc"
print(palindrome(s))
print(valid_palindrome(s))
