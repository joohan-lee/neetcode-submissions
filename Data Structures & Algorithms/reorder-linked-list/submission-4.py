# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHead = slow.next
        slow.next = None # Cut the first and second
        # Reverse second half
        newHead = self.reverse(secondHead)
        # Merge them
        self.merge(head, newHead)
    
    def reverse(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while l1:
            tmp = l1.next
            l1.next = prev
            prev = l1
            l1 = tmp
        return prev
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> None:
        is_l1_turn = True
        while l1 and l2:
            if is_l1_turn:
                tmp = l1.next
                l1.next = l2
                l1 = tmp
            else:
                tmp = l2.next
                l2.next = l1
                l2 = tmp
            is_l1_turn = not is_l1_turn
        
        # if l1:
        #     l2.next = l1
        # if l2:
        #     l1.next = l2
        

