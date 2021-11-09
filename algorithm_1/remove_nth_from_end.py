# No. 19

def removeNthFromEnd(head, n):
    i = j = head
    
    for _ in range(n):
        i = i.next
        
    if not i:
        return j.next
    
    while i.next:
        i = i.next
        j = j.next
        
    j.next = j.next.next
    
    return head