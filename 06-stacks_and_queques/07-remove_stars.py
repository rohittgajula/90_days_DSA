# Choose a star in s
# Remove the closest non-star character to its left, as well as remove the star itself.

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

