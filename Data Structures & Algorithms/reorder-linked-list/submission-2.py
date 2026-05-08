# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Split list into two
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHead = slow.next # 두번째 head를 먼저 저장 후
        slow.next = None # Cut the first and second

        # 2. Reverse the second half
        newHead = self.reverse(secondHead)

        # 3. Merge them
        self.merge(head, newHead)
    
    def reverse(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        return prev
    
    def merge(self, head1, head2):
        # [1,2,3,4,5] => [1,5,2,4,3]
        # [1,2,3,4] => [1,4,2,3]
        while head1 and head2:
            tmp1 = head1.next
            head1.next = head2
            head1 = tmp1

            tmp2 = head2.next
            head2.next = head1
            head2 = tmp2

