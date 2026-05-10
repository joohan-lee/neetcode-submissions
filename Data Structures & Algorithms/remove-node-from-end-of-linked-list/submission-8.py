# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Recursion solution
        dummy = ListNode()
        dummy.next = head
        def helper(node):
            if not node:
                return 0
            idx = helper(node.next) + 1 # idx from the end
            if idx == n + 1: # 삭제 직전 노드
                node.next = node.next.next
            return idx
        
        helper(dummy)
        return dummy.next