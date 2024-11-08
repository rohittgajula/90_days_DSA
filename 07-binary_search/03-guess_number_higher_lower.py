



# this is available in leetcode bcz guess() function is not available here


def guessNumber(self, n):
        l = 0
        r = n
        while l <= r:
            m = (l+r)//2
            res = guess(m)      # guess is a function in leetcode
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m


n = 10
pick = 6
print(guessNumber(n))

