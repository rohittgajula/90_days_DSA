

def remove_stars(s):
    stack = []
    for char in s:
        if char == "*":
            stack.pop()
            continue
        else:
            stack.append(char)
    return "".join(stack)


s = "leet**cod*e"
print(remove_stars(s))

