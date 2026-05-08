# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, d):
            nonlocal res
            if not node:
                return 0
            
            res = max(res, d)
            if node.left:
                helper(node.left, d + 1)
            if node.right:
                helper(node.right, d + 1)
            
            

        helper(root, 1)
        return res
        