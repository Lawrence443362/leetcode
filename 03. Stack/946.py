# 946. Validate Stack Sequences
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        i, j = 0, 0

        while i < len(pushed):
            stack.append(pushed[i])

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
            i += 1
                        
        while j < len(popped):
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False 
            
        if stack == []: 
            return True
        else: 
            return False