# 876. Middle of the Linked List
class Solution:
    def middleNode(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow