

def reverse_polish_notation(tokens):
    stack = []
    operations = ['+','-','*','/']
    for char in tokens:
        if char in operations:
            a = stack.pop()
            b = stack.pop()
            if char == "+":
                stack.append(b + a)
            elif char == "-":
                stack.append(b - a)
            elif char == "*":
                stack.append(b * a)
            elif char == "/":
                stack.append(int(float(b) / a))
        else:
            stack.append(int(char))
    return stack[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(reverse_polish_notation(tokens))