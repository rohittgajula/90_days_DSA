from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        # Append the new element
        self.q.append(x)
    
    def pop(self):
        # Rotate all elements except the last one to the front of the queue
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        # Pop the last remaining element
        return self.q.popleft()

    def top(self):
        # Similar to pop but keeps the last element
        res = None
        for _ in range(len(self.q)):
            res = self.q.popleft()
            self.q.append(res)
        return res
    
    def empty(self):
        return len(self.q) == 0
    

obj = MyStack()
obj.push(5)
obj.push(10)
print(obj.top())     # Outputs 10
print(obj.pop())     # Outputs 10
print(obj.empty())   # Outputs False
print(obj.pop())     # Outputs 5
print(obj.empty())   # Outputs True
