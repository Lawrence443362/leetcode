# 2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        remainder = 0
        while l1 or l2:
            val1, val2 = self.getValue(l1), self.getValue(l2)
            sum = val1 + val2 + remainder

            if sum <= 9:
                current.next = ListNode(sum)
                current = current.next
                l1 = self.getNextNode(l1)
                l2 = self.getNextNode(l2)
                remainder = 0
            else:
                current.next = ListNode(sum % 10)
                current = current.next
                l1 = self.getNextNode(l1)
                l2 = self.getNextNode(l2)
                remainder = 1

        if remainder == 1: 
            current.next = ListNode(1)

        return dummy.next

    def getValue(self, node):
        if node:
            return node.val
        else:
            return 0 
        
    def getNextNode(self, node):
        if node:
            return node.next
        else:
            return None

        