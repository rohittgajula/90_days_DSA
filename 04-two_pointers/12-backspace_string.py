

def backspace_string(s, t):
    
    if check(s) == check(t):
        return True
    else:
        return False


def check(word):
    stack = []
    for i in word:
        if i != "#":
            stack.append(i)
        elif not stack:
            continue
        else:
            stack.pop()
    return "".join(stack)


s = "a##c"
t = "#a#c"
print(backspace_string(s, t))