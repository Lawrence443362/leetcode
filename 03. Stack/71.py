# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")
        stack = []

        for item in items:
            if item in ["", "."]:
                continue
            elif stack and item == "..":
                stack.pop()
            elif item != "..": 
                stack.append(item)

        return "/" + "/".join(stack)