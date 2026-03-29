# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode
        head = res

        carry= 0

        while l1 or l2 or carry:

            cSum = 0
            if l1:
                cSum +=l1.val
                l1 = l1.next
            if l2:
                cSum += l2.val
                l2 = l2.next
            
            cSum += carry
            digit = cSum%10
            carry = cSum //10

            res.next = ListNode(digit)
            res = res.next
        return head.next