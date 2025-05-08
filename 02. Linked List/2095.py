# 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head):
        slowest = head
        slow, fast = head, head
        if fast and fast.next:
            while fast and fast.next:
                slowest = slow
                slow = slow.next
                fast = fast.next.next
            slowest.next = slow.next

            return head
        else:
            return 
