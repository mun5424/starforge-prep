class MyQueue(object):
    def __init__(self):
        self.main_stack = []
        self.reverse_stack = []

    def push(self, x):
        self.main_stack.append(x) 

    def pop(self):
        self.peek()
        return self.reverse_stack.pop()

    def peek(self):
        if not self.reverse_stack: 
            while self.main_stack:
                self.reverse_stack.append(self.main_stack.pop()) 
        return self.reverse_stack[-1] 

    def empty(self):
        return not self.main_stack and not self.reverse_stack