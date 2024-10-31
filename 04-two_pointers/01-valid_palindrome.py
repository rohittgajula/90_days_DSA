
def palindrome(s):
    
    l = 0
    r = len(s)-1

    while l < r:
        # check l-pointer is alp or not
        while l < r and not is_alnum(s[l]):
            l += 1
        # check r-pointer is alp or not
        while r > l and not is_alnum(s[r]):
            r -= 1
        # check both l and r pointer alp are same
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

# converting alp to ascii values to compare
def is_alnum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

s = "A man, a plan, a canal: Panama"
print(palindrome(s))

