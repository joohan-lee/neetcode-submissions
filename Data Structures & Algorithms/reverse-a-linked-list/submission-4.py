# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive way
        
        if not head or not head.next:
            return head
        
        # 새로운 head는 위로 계속 보내줌.
        newHead = self.reverseList(head.next)
        head.next.next = head # 다음 노드가 나를 가리키게 하고, 내 next는 끊어둠.
        head.next = None

        return newHead