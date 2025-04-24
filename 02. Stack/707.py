# 707. Design Linked List
class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
            


    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size += 1        

    def addAtTail(self, val: int) -> None:
        node = Node(val)

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
            prev.next = Node(val, prev.next)
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
        

    