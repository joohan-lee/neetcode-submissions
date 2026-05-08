# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Divide into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None # 절단.
        # 2. Reverse second one
        newHead = self.reverseList(middle)
        # 3. Merge first half and reversed second half
        while head and newHead:
            tmp1, tmp2= head.next, newHead.next
            head.next = newHead
            newHead.next = tmp1
            head, newHead = tmp1, tmp2
    
    def reverseList(self, node):
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev
