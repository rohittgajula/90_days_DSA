# Write a function to calculate the factorial of a number using recursion and iteration.


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_recursion(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


n = 10
print(factorial(n))
print(factorial_recursion(n))

