# Check Balanced Brackets: Check if the given string has balanced parentheses/brackets ({[()]}).


def valid_parenthesis(s):
    hashMap = {'}':"{", "]":"[", ")":"("}
    stack = []

    for char in s:
        if char not in hashMap:
            stack.append(char)
        else:
            if not stack:
                return False
            pooped = stack.pop()
            if pooped != hashMap[char]:
                return False
    
    return True if not stack else False


s = "{[()()]}"
print(valid_parenthesis(s))