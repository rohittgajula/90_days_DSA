# Write a function to calculate the sum of the digits of a number.


def sum_of_digits(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


n = 10
print(sum_of_digits(n))