# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class ListNode:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = (v1 + v2 + carry) % 10
            
            node = ListNode(v)
            prev.next = node
            prev = prev.next

            carry = (v1 + v2 + carry) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        

            