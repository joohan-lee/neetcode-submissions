# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 2개 씩 머지. O(n logm), where n is maximum length of list, m is the lenght of lists
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoList(l1, l2))
            lists = mergedLists
        
        return lists[0]
    
    def mergeTwoList(self, l1:ListNode, l2:Optional[ListNode]) -> ListNode:
        prev = dummy = ListNode()
        if not l2:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        
        return dummy.next
