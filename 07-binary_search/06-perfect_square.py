
# binary search         time comp = log(n)
def isPerfectSquare(num):
    left = 1
    right = num

    while left <= right:
        middle = (left + right) // 2
        if middle * middle > num:
            right = middle - 1
        elif middle * middle < num:
            left = middle + 1
        else:
            return True
    return False


# brute force solution. time comp = (sqrt(n))
def perfect_square(num):
    i = 0
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False


num = 16
print(isPerfectSquare(num))
print(perfect_square(num))

