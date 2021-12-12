class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        i = 0
        tmp = self.head
        while tmp and i < index:
            tmp = tmp.next
            i += 1
        return tmp.val
            
    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
        else:
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head
        self.size += 1
    
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head
            self.size += 1
        elif index > 0 and index <= self.size - 1:
            i = 0
            tmp = self.head
            while i < index - 1:
                tmp = tmp.next
                i += 1
            old_next = tmp.next
            tmp.next = Node(val)
            tmp.next.next = old_next
            self.size += 1
        elif index == self.size:
            i = 0
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(val)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head.next:
                self.head = self.head.next
                self.size -= 1
        if index > 0 and index <= self.size - 1:
            i = 0
            tmp = self.head
            while i < index - 1:
                tmp = tmp.next
                i += 1
            tmp.next = tmp.next.next
            self.size -= 1

    def print(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        print(arr)


l = MyLinkedList()
l.addAtHead(1)
l.print()

l.addAtTail(3)
l.print()

l.addAtIndex(1,2)
l.print()

print('got:', l.get(1))

l.deleteAtIndex(1)
l.print()

print('got:', l.get(1))
print('got:', l.get(3))

l.deleteAtIndex(3)
l.print()

l.deleteAtIndex(0)
l.print()

print('got:', l.get(0))

l.deleteAtIndex(0)
l.print()

print('got:', l.get(0))



        