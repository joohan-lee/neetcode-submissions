# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        When we pass to the upper level, max(left+root, right +root, root)
        But we need to check (left + root +right) can be the maximum as well.
        """
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            curr_max = max(left + node.val, right + node.val, node.val)
            res = max(res, curr_max, left+right+node.val)

            return curr_max
        
        dfs(root)
        return res
        
        