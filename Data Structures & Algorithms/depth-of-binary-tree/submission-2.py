# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxLevel = 0

        def dfs(node, level):
            if not node:
                return
            nonlocal maxLevel
            maxLevel = max(maxLevel, level)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 1)
        return maxLevel