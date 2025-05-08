# 1721. Swapping Nodes in a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k):
        left = self.getLeft(head, k)
        right = self.getRight(head, k)

        left.val, right.val = right.val, left.val

        return head

    def getLeft(self, head, k):
        current = head
        
        for _ in range(1, k):
            current = current.next

        return current
    
    def getRight(self, head, k):
        slow, fast = head, head

        for _ in range(k): 
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow