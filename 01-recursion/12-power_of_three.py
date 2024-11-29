# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.


def power_three(n):
    if n <= 0:
        return False
    x = 1
    while x <= n:
        if x == n:
            return True
        x *= 3
    return False


# recursion
def powerOfThree(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    
    if n % 3 != 0:
        return False
    return powerOfThree( n // 3)



n = 27
print(power_three(n))
print(powerOfThree(n))