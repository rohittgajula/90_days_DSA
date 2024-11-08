

def simplify_path(path):
    stack = []
    components = path.split("/")

    for component in components:
        if component == "..":
            if stack:
                stack.pop()
        elif component and component != ".":
            stack.append(component)

    return "/"+"/".join(stack)


path = "/home/"
print(simplify_path(path))