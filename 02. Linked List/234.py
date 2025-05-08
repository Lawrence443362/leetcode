# 234. Palindrome Linked List
class Solution:
    def isPalindrome(self, head):
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        left, right = 0, len(stack) - 1

        while left < right:
            if stack[left] != stack[right]:
                return False
            
            left += 1
            right -= 1 

        return True