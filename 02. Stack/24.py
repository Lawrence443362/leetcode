# 24. Swap Nodes in Pairs
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        current = head
        prev = None
        result = self.getHead(head)
        while current and current.next: 
            n1 = current
            n2 = n1.next
            n3 = n2.next

            n1.next = n3
            n2.next = n1

            if prev != None:
                prev.next = n2

            prev = current                
            current = current.next

        return result

    def getHead(self, head):
        if head == None: 
            return None
        elif head.next == None:
            return head
        else:
            return head.next