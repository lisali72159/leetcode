# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a1 = two = ListNode(2)
four = ListNode(4)
three = ListNode(3)
two.next = four
four.next = three
# (2 -> 4-> 3)

five = ListNode(5)
six = ListNode(6)
four_ = ListNode(4)
five.next = six.next = four_
# (5 -> 6 -> 4)



def addTwoNumbers(l1, l2):
    curr1 = l1
    curr2 = l2
    carry = 0
    resultCurr = None
    result = None

    while curr1 is not None:
        sum = curr1.val + curr2.val + carry
        carry = sum // 10
        digit = sum % 10
        nextNode = ListNode(digit)
        
        if resultCurr is None:
            resultCurr = nextNode
            result = resultCurr
        else: 
            resultCurr.next = nextNode
            resultCurr = resultCurr.next
            
        curr1 = curr1.next
        curr2 = curr2.next

        if carry == 1
            resultCurr.next = ListNode(carry)

    return result

addTwoNumbers(a1,b1)

#edge scenarios: different lengths of 2 linked lists, result is different length if there is a carry 
