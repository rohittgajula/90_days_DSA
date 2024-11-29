# ASCII sheet : https://www.ascii-code.com/characters/printable-characters

# ord is used to find ASCII value of a char
class Solution:
    def is_palindrome_without_inbuilt_fun(self, s):
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while r > l and not self.isalnum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    # helper function - ord is used to find ASCII values.
    def isalnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
                )
    
# -----------------------------------


def isPalindrome(s):
    if s is None or len(s) <= 1:
        return True

    l, r = 0, len(s)-1
    while l<r:
        left = s[l].lower()
        while not ('a' <= left <= 'z' or '0'<=left<='9') and l<r:
            l += 1
            left = s[l].lower()
            
        right = s[r].lower()
        while not ('a' <= right <= 'z' or '0'<=right<='9') and l<r:
            r -= 1
            right = s[r].lower()
        
        if left != right:
            return False
        else:
            l += 1
            r -= 1
    return True


def is_palindrome_with_inbuilt_function(s):
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


s = "A man, a plan, a canal: Panama"

solution = Solution()
print(solution.is_palindrome_without_inbuilt_fun(s))
print(isPalindrome(s))
print(is_palindrome_with_inbuilt_function(s))