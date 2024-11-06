

def daily_tempratures(temperatures):

    res = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)
    return res
    

def dailyTempratures(temperatures):

    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res



temperatures = [73,74,75,71,69,72,76,73]
print(daily_tempratures(temperatures))
print(dailyTempratures(temperatures))

