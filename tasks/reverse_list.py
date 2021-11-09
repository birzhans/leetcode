# No. 206

def reverse_list(head):
    if not head or not head.next:
        return head
    
    prev = None
    
    while head.next:
        old_head = head
        old_next = head.next
        head.next = prev
        
        prev = old_head
        head = old_next
     
    head.next = prev
                    
    return head