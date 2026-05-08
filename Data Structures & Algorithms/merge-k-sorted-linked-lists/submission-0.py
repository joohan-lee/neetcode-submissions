# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1->2->4
        1->3->5
        3->6

        """
        l = []
        for curr in lists:
            while curr:
                l.append(curr.val)
                curr = curr.next

        l.sort()
        
        dummy = ListNode()
        prev = dummy
        for i in range(len(l)):
            node = ListNode(l[i])
            prev.next = node
            prev = node
        
        return dummy.next
