# Reverse a String: Write a function to reverse a string without using Python's [::-1] slicing.


def reverseString(s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

s = "hello world"
print(reverseString(s))

