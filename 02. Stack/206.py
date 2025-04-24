# 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        reversed_list = None
        current = head

        while current:
             reversed_list = ListNode(current.val, reversed_list)
             current = current.next
        
        return reversed_list
        