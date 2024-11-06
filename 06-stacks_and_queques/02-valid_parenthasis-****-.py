

def is_valid_parentheses(s):
    hashMap = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        # If character is an opening parenthesis (not in hashMap), push it onto the stack
        if c not in hashMap:
            stack.append(c)
        else:
            # If stack is empty and we find a closing parenthesis, it’s invalid
            if not stack:
                return False
            # Pop the top element from the stack (most recent opening parenthesis)
            popped = stack.pop()
            # Check if the popped element matches the current closing parenthesis
            if popped != hashMap[c]:
                return False
    
    return True if not stack else False

s = "(())[]{}"
print(is_valid_parentheses(s))
