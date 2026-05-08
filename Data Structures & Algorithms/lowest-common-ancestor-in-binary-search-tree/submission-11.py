# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p.val > q.val:
            p, q = q, p
        
        if q.val < root.val:
            # 더 큰 값이 root보다 작으면 왼쪽만 보면됨.
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            # 우측만 탐색
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # p.val < root.val < q.val or (p.val == root.val and root.val < q.val) or (p.val < root.val and root.val == q.val)
            return root