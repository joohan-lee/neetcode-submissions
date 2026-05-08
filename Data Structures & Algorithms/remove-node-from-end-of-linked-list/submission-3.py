# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(head):
            nonlocal n
            # Base case
            if not head:
                return None
            
            head.next = helper(head.next) # just connect
            n -= 1
            if n == 0:
                # If n-th node from the end, remove
                return head.next

            return head
        
        return helper(head)
        