# Write a function to generate the first n Fibonacci numbers.


def fibonachiSeries(n):
    
    res = [0, 1]
    for i in range(2, n):
        res.append(res[-1] + res[-2])
    return res


def fibonachiWithRecursion(n):

    if n <= 1:
        return n
    else:
        return fibonachiWithRecursion(n-1) + fibonachiWithRecursion(n-2)


n = 10
print(fibonachiSeries(n))
fibonachiWithRecursion(n)