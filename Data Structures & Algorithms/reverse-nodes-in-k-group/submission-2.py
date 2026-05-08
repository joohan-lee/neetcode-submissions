# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # group의 첫 노드는 다음 그룹의 첫 노드에 미리 연결.
        # groupPrev는 kth와 연결하여 이전 그룹이 현재 그룹 오리지널 순서의 마지막을 가리키도록.
        dummy = ListNode()
        groupPrev = dummy
        groupPrev.next = head

        while True:
            kth = self.get_kth(groupPrev, k) # 현재 그룹 마지막 노드.
            if not kth:
                # 만약 현재 그룹이 k개 노드보다 작으면 reverse 안함.
                break
            
            groupNext = kth.next # 다음그룹의 첫 노드.

            # Reverse current group
            prev, curr = groupNext, groupPrev.next # 보통은 prev는 None이지만 여기서는 현재 그룹 첫 노드는 다음 그룹 첫 노드를 가리키도록
            for i in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 이전그룹이 현재 마지막 노드 가리키도록 하고 이전그룹 마지막 노드 위치를 업데이트
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
    
    def get_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
