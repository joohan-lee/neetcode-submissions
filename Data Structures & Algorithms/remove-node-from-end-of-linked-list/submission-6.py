# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left.next = head
            left = left.next
            head = head.next
            right = right.next
        
        left.next = head.next
        return dummy.next