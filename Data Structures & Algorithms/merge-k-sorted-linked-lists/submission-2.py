# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    """
    min heap은 기본적으로 숫자 간 비교인데, node.val을 비교하기 위한 wrapper
    """
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        5       7      3       8
           5->7           3->8
                3->5->7->8

        """
        # heap에 각 list의 head (minimum)을 넣어놓고 하나씩 빼면서 next로 넘기고 그 값을 또 heap에 넣기.
        min_heap = []
        for lst in lists:
            if lst:
                heapq.heappush(min_heap, NodeWrapper(lst))
        
        dummy = ListNode()
        prev = dummy
        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            node = node_wrapper.node
            
            prev.next = node
            if node.next:
                heapq.heappush(min_heap, NodeWrapper(node.next))
            prev = node
        
        return dummy.next

        # dummy = ListNode()
        # cur = dummy

        # while True:
        #     minNode = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if minNode == -1 or lists[minNode].val > lists[i].val:
        #             minNode = i
                
        #     if minNode == -1:
        #         # 모든 node 다 돌았음.
        #         break
            
        #     cur.next = lists[minNode]
        #     lists[minNode] = lists[minNode].next
        #     cur = cur.next
        # return dummy.next