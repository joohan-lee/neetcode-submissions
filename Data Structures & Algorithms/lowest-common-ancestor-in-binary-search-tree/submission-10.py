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
        
        if (p.val < root.val < q.val) or (p.val == root.val and root.val < q.val) or (q.val == root.val and root.val > p.val):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right=self.lowestCommonAncestor(root.right, p, q)

        if left:
            return left
        if right:
            return right
        
        return None