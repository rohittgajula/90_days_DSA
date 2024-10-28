
# with builtin methods
def make_good(s):
    stack = []
    i = 0
    while i < len(s):
        if (
            stack and
            stack[-1] != s[i] and
            stack[-1].lower() == s[i].lower()
            ):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    return "".join(stack)



def makeGood(s):
    stack = []
    for char in s:
        if stack:
            if (char.lower() == stack[-1].lower()) and (char.islower() != stack[-1].islower()):
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    return ''.join(stack)

s = "leEeetcode"
print(make_good(s))
print(makeGood(s))

