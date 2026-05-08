# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        
        for i in range(n):
            second = second.next
        
        prev = dummy = ListNode()
        while second:
            prev.next = first
            prev = prev.next
            first = first.next
            second = second.next
        
        prev.next = first.next
    
        return dummy.next
        
