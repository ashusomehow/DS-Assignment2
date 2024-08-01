class ListN:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.dummy = ListN(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListN(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = ListN(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        new_node = ListN(val)
        new_node.next = curr.next
        curr.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.length -= 1
