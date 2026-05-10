# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()
        while head:
            if head in st:
                return True
            st.add(head) # Python hash object's memory addr and create own id.
            head = head.next
        return False