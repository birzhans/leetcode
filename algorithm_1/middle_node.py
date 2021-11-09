# No. 876

def middleNode(head):
    i = j = head
    while j and j.next:
        i = i.next
        j = j.next.next
    return i