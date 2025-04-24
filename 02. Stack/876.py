# 876. Middle of the Linked List
import math

class Solution:
    def middleNode(self, head):
        size = self.calcSize(head)
        middle = self.calcMiddle(size)
        list = LinkedList(head, size)

        return list.get(int(middle) - 1)


    def calcMiddle(self, size):
        if size % 2 == 0:
            return size / 2 + 1
        else:
            return math.ceil(size / 2)

    def calcSize(self, head):
        if head != None:
            size = 0
            current = head
            while current:
                size += 1
                current = current.next
            return size


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class LinkedList:

    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        current = self.head
        for _ in range(index):
            current = current.next
        return current
            


    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        if self.size == 0:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = ListNode(val, prev.next)
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        if self.size != 0:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
            else:
                prev = self.head
                for _ in range(index - 1):
                    prev = prev.next
                if prev.next != None:
                    prev.next = prev.next.next
                    self.size -= 1
        

    