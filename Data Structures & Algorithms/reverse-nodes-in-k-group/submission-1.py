# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0 # 현재 그룹의 노드 수
        while cur and group < k:
            cur = cur.next
            group += 1
        
        
        if group == k:
            cur = self.reverseKGroup(cur, k) # 다음 그룹의 첫 노드
            while group > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                group -= 1
            
            head = cur # reverse한 후의 현재 마지막 노드를 head로.
        
        return head # 현재 그룹의 head(첫 노드)를 리턴해서 이전 그룹의 마지막 노드를 연결

