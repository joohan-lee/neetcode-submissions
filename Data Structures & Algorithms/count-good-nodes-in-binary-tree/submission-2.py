# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, curr_max):
            nonlocal res
            if not node:
                return None
            
            if node.val >= curr_max:
                res += 1
            
            dfs(node.left, max(curr_max, node.val))
            dfs(node.right, max(curr_max, node.val))
        
        dfs(root, -float('inf'))
        return res