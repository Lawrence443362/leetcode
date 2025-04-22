# Backspace String Compare
class Solution(object):
    def backspaceCompare(self, s, t):
        return self.format_string(s) == self.format_string(t)
    
    def format_string(self, string):
        queue = []

        for i in string:
            if i != "#":
                queue.append(i)
            else:
                if len(queue) > 0:
                    queue.pop()
        
        return "".join(queue)