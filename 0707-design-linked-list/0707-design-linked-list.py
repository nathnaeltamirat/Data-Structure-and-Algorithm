class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0)

    def get(self, index: int) -> int:
        count = -1
        current = self.dummy.next
        while current:
            count += 1
            if count == index:
                return current.val
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.dummy.next:
            self.dummy.next = ListNode(val)
            return
        secondNext = self.dummy.next
        NewNode = ListNode(val)
        self.dummy.next = NewNode
        NewNode.next = secondNext
    def addAtTail(self, val: int) -> None:
        curr = self.dummy.next
        if not curr:
            self.dummy.next= ListNode(val)
            return
        prev = None
        while curr:
            prev = curr
            curr = curr.next
        prev.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        count = 0
        current = self.dummy.next
        if not current and index == 0:
            self.dummy.next = ListNode(val)
            return
        prev = None
        while current:
            if count == index:
                if not prev:
                    second = self.dummy.next
                    newNode = ListNode(val)
                    self.dummy.next = newNode
                    newNode.next = second
                    return
                else:
                    newNode = ListNode(val)
                    prev.next = newNode
                    newNode.next = current
                return
            prev = current
            current = current.next
            count += 1
        if count == index:
            prev.next = ListNode(val)
            return
        return -1
    def deleteAtIndex(self, index: int) -> None:
        count = 0
        current = self.dummy.next

        prev = None
        while current:
            if count == index:
                if not prev:
                    self.dummy.next = self.dummy.next.next
                    return
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            count += 1

        return -1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)