# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        5       7      3       8
           5->7           3->8
                3->5->7->8
        
        adjacent한 list 끼리 병합. (O(n))
        이를 최대 log_2_k 번하므로,
        총 O(n*logk) 걸림.
        """
        
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None

                mergedLists.append(self.mergeTwoList(l1, l2))
            
            lists = mergedLists
        
        return lists[0]
    
    def mergeTwoList(self, l1, l2):
        dummy = ListNode()
        prev = dummy

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
                prev = prev.next
            else:
                prev.next = l2
                l2 = l2.next
                prev = prev.next
        
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        
        return dummy.next
