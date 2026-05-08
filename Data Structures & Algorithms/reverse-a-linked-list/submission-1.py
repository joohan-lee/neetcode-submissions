# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 아무것도 없을 때는 head.next 조차 없으므로 early return
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head # 앞의 노드를 나를 가리키게 함.
        head.next = None # 현재 노드의 다음은 끊어둠.

        return newHead # 마지막 노드를 위로 계속 보내줌.