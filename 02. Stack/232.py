# 232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.empty != False: 
            return self.items.pop(0)


    def peek(self):
        if self.items != []: 
            return self.items[0]

    def empty(self):
        return self.items == []        
