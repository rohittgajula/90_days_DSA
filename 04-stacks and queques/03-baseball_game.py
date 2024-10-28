


def baseball_game(ops):
    stack = []

    for char in ops:
        if char == "C":
            stack.pop()
        elif char == "D":
            stack.append(2 * stack[-1])
        elif char == "+":
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(char))
    return sum(stack)

ops = ["5","-2","4","C","D","9","+","+"]
print(baseball_game(ops))


