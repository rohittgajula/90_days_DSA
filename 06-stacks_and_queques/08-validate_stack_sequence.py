


def validate_stack_sequence(pushed, popped):
    stack = []
    i = 0
    j = 0

    while i < len(pushed):
        stack.append(pushed[i])
        i += 1

        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        
    return len(stack) == 0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validate_stack_sequence(pushed, popped))

