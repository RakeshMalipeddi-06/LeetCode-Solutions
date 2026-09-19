
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        if index < 0 or index >= self.length:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1

    def addAtTail(self, val):
        node = Node(val)

        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def addAtIndex(self, index, val):
        if index > self.length:
            return

        if index <= 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        curr = self.head

        for _ in range(index):
            curr = curr.next

        node = Node(val)

        node.prev = curr.prev
        node.next = curr
        curr.prev.next = node
        curr.prev = node

        self.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return

        curr = self.head

        for _ in range(index):
            curr = curr.next

        if self.length == 1:
            self.head = self.tail = None

        elif curr == self.head:
            self.head = self.head.next
            self.head.prev = None

        elif curr == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.length -= 1