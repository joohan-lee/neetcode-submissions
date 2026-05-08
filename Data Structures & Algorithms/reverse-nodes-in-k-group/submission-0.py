# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # 이전 그룹의 마지막 노드

        while True:
            kth = self.getKth(groupPrev, k) # 현재 그룹 마지막 노드 (k번째)
            if not kth:
                # k번쨰 노드가 없다는 말은 list가 끝남.
                break
            
            groupNext = kth.next # 다음 그룹의 첫번째 노드.

            # Reverse current group
            prev, curr = groupNext, groupPrev.next # 보통은 prev는 None이지만 그러면 linked list가 끊기므로 현재 그룹 첫 노드는 다음 그룹 첫 노드를 가리키도록
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next # 이전 그룹의 next는 현재 그룹 첫 노드. 이를 임시 저장
            groupPrev.next = kth # 이전 그룹의 next를 현재 그룹 마지막 노드로 연결. (reverse 했으므로)
            groupPrev = tmp # groupPrev를 현재 그룹으로 옮김.
        
        return dummy.next


    
    def getKth(self, curr, k):
        i = 0
        while curr and i < k:
            i += 1
            curr = curr.next
        return curr