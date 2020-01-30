def remove_ele(head, val):
    dummy = Node(None)
    dummy.next = head

    node = head
    prev = dummy

    while node:
        if node.val == val:
            prev.next = node.next
        else:
            prev = prev.next
        node = node.next
    return dummy.next