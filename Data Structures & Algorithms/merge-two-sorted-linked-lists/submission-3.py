# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        curr = dummy = ListNode()
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

        # Recursion


        # """
        # 재귀로 풀 때: head 결정 → 나머지 subproblem 위임
        # """
        # # Part 1: Base Case - 한쪽이 끝나면 나머지 그대로 붙이기
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        
        # # Part 2 & 3: 작은 쪽이 head가 되고, 나머지는 재귀에 맡김 
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)# "내 뒤는 네가 알아서 해"
        #     return l1 # "난 head야"
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        