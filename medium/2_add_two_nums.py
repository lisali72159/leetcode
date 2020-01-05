# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
# (2 -> 4-> 3)

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
# (5 -> 6 -> 4)


def addTwoNumbers(l1, l2):
    curr1 = l1
    curr2 = l2
    carry = 0
    resultCurr = None
    result = None

    while curr1 or curr2:
        val1 = curr1.val if curr1 else 0 #Python ternary
        val2 = curr2.val if curr2 else 0 
        sum = val1 + val2 + carry
        carry = sum // 10
        digit = sum % 10
        nextNode = ListNode(digit)
        
        if resultCurr is None:
            resultCurr = nextNode
            result = resultCurr
        else: 
            resultCurr.next = nextNode
            resultCurr = resultCurr.next
            
        if curr1: curr1 = curr1.next
        if curr2: curr2 = curr2.next

        if carry == 1:
            resultCurr.next = ListNode(carry)

    return result



# Edge-case scenarios: different lengths of 2 linked lists, result is different length if there is a carry 
# Time Complexity: O(n) where n is the length of longest list or O(max(m,n)) 
# Space Complexity: O(n) where n is the length of longest list

def _addTwoNumbers(l1, l2, carry = 0):
    if l1 is None and l2 is None:
        return None

    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    sum = val1 + val2 + carry
    carry = sum // 10
    digit = sum % 10
    newNode = ListNode(digit)

    newNode.next = addTwoNumbers(l1.next, l2.next, carry)