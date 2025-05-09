# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next