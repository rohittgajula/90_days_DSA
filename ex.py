

def is_valid(s):
    hashMap = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in hashMap:
            stack.append(c)
        else:
            if not stack:
                return False
            pooped = stack.pop()
            if pooped != hashMap[c]:
                return False
    return True if not stack else False



s = "()[]{}"
print(is_valid(s))