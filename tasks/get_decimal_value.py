# No 1290

def get_decimal_value(head):
    num = head.val
    
    while head.next:
        num = num * 2 + head.next.val
        head = head.next
    return num