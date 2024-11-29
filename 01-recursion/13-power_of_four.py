# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.


def isPowerFour(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    
    if n % 4 != 0:
        return False
    return isPowerFour( n // 4)

n = 16
print(isPowerFour(n))

