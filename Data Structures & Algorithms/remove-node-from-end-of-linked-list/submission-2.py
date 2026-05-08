# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        쭉 stack에 재귀를 쌓아서 들어가다가,
        되돌아 나올 때 n-th to last를 제거.
        .next를 변경해야 하나가 제거될 수 있으므로,
        .next에 이어붙여야함.
        """
        def helper(head):
            nonlocal n
            if not head:
                return None
            
            head.next = helper(head.next)
            n -= 1
            if n == 0:
                return head.next
            return head 
        return helper(head)