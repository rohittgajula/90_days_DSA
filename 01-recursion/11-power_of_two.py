# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.


def isPowerOfTwo(n):
    if n <= 0:
        return False
    x = 1
    while x <= n:
        if x == n:
            return True
        x *= 2
    return False

def isPower_recursion(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:                              # this case applies for n = 3
        return False
    return isPower_recursion(n // 2)            # n is divided by 2 until it reaches 1, thus 1 is true.

n = 16
print(isPowerOfTwo(n))
print(isPower_recursion(n))

