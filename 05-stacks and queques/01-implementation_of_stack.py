
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    def push(self, item):
        self.stack.append(item)
        return f'{item} pushed to stack.'
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    
    def display(self):
        return f'Stack : {self.stack}'
    

stack = Stack()
print(f'Push : {stack.push(10)}')
print(f'Push : {stack.push(20)}')
print(f'Push : {stack.push(30)}')
print(f'Display : {stack.display()}')
print(f'Size : {stack.size()}')
print(f'Peek (top element) : {stack.peek()}')
print(f'Pop (remove top element) : {stack.pop()}')
print(f'Display : {stack.display()}')
print(f'Peek : {stack.peek()}')
print(f'Size : {stack.size()}')
print(f'Is empty : {stack.is_empty()}')



