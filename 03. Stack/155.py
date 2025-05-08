# 155. Min Stack
class MinStack:
    def __init__(self):
        self.min_value = None
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_value == None or self.min_value > val:
            self.min_value = val

    def pop(self) -> None:
        if self.stack and self.stack[-1] != self.min_value: 
            self.stack.pop()
        elif self.stack and self.stack[-1] == self.min_value:
            self.stack.pop()
            if self.stack: 
                self.min_value = min(self.stack)
            else:
                self.min_value = None       

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value
        
