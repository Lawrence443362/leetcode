# 82. Remove Duplicates from Sorted List II
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == None: 
            return None
        elif head.next == None:
            return head
        
        dummy = ListNode()
        current = dummy

        slow, fast = head, head

        while slow and fast:
            if slow.val != fast.val and slow.val != slow.next.val: 
                current.next = ListNode(slow.val)
                current = current.next
                slow = fast
                fast = fast.next
            elif slow.val != fast.val and slow.val == slow.next.val:
                slow = fast
                fast = fast.next
            else: 
                fast = fast.next

        if slow.next == None:
            current.next = ListNode(slow.val)
            
        return dummy.next