# https://youtu.be/5rHz_6s2Buw

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.


# optimal solution - we cannot directly solve this question
def arrangeCoins(n):
    # Initialize the search range from 1 to n
    l = 1
    r = n
    
    # Variable to store the result, which will track the maximum number of complete rows
    res = 0

    # Perform binary search to find the maximum number of rows we can fully fill
    while l <= r:
        # Calculate the midpoint of the current range
        mid = (l + r) // 2
        
        # Calculate the total coins needed to fill `mid` rows using the formula for the sum of the first `mid` natural numbers
        coins = (mid / 2) * (mid + 1)
        
        # If the calculated coins exceed `n`, reduce the search space by moving `r` to the left
        if coins > n:
            r = mid - 1
        else:
            # If `mid` rows can be completed with the available coins, adjust the lower bound to search for potentially more rows
            l = mid + 1
            # Update `res` to the maximum rows found so far
            res = max(mid, res)
    
    # Return the result, which is the maximum number of complete rows that can be formed
    return res




# brute force solution.
def arrange_coins(n):
    row = 1                 # starts with 1st row requiring 1 coin
    complete_rows = 0       # track no of complete rows

    while n >= row:
        n -= row            # use `row` coins for the current row
        complete_rows += 1
        row += 1
    return complete_rows

n = 5
print(arrangeCoins(n))
print(arrange_coins(n))