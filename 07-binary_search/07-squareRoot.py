# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.


def squareRoot(x):
    if x < 2:
        return x
    
    left = 0
    right = x

    while left <= right:
        middle = (left + right) // 2
        mid_square = middle * middle

        if mid_square == x:
            return middle
        elif mid_square < x:
            left = middle + 1
        else:
            right = middle - 1
    return right

x = 5
print(squareRoot(x))

