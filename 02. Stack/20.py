# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        stack = []

        for i in s: 
            if i in parentheses:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                p = stack.pop()
                if parentheses[p] != i:
                    return False


        if len(stack) != 0:
            return False
        else:
            return True