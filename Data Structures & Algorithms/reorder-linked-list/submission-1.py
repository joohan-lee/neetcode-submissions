# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Store all nodes in an array
        if not head:
            return None
        
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        i, j = 0, len(nodes) - 1

        while i < j:
            temp = nodes[i].next
            nodes[i].next = nodes[j]
            nodes[j].next = temp
            i += 1
            j -= 1
        nodes[i].next = None # 마지막 노드의 next를 None으로 끊어줘야함.
            