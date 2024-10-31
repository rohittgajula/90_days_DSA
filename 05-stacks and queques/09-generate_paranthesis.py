


def generate_paranthesis(n):
    # only add open paranthesis if open < n
    # only add closing paranthesis if closed < open
    # valid closed == open == n

    stack = []
    result = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            result.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0,0)
    return result

def generateParenthesis(n):
    def handle(l,r,s):
        if len(s)==n*2:
            res.append(s)
            return
        if l<n:
            handle(l+1,r,s+'(')
        if r<l:
            handle(l,r+1,s+')')
    res=[]
    handle(0,0,'')
    return res

n = 3
print(generate_paranthesis(n))
print(generateParenthesis(n))

