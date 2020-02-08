# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

#  Reverse a singly-linked list

def reverseLinkedList(head):
    prev = None
    temp = head
    current = head
    
    while current:
        temp = head.next
        curr.next = prev
        prev = current
        current = temp
    
    return prev