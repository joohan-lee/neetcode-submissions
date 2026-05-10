# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # One Pass. Two pointers
        right = head
        while n > 0:
            right = right.next
            n -= 1
        
        prev = dummy = ListNode()
        left = head
        while right:
            prev.next = left
            prev = prev.next
            left = left.next
            right= right.next
        prev.next = left.next

        return dummy.next
        