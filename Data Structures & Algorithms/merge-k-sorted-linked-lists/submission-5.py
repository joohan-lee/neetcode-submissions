# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 2개 씩 머지. O(n logm), where n is the total number of nodes in m lists, m is the lenght of lists
        # Divide and Conquer. Recursive. 
        if not lists:
            return None
        return self.divide(lists, 0, len(lists) - 1)
    
    def divide(self, lists, l, r) -> ListNode:
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        mid = l + (r-l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid+1, r)
        return self.mergeTwoList(left, right) # Conquer
    
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
