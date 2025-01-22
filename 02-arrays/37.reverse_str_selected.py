

def ans(s, k):
    if k in s:
        index = s.index(k)
        reversed_str = s[:index][::-1]
        remaining_str = s[index+1:]
    return reversed_str + remaining_str


s = "rohit"
k = "h"
print(ans(s, k))            # orit

