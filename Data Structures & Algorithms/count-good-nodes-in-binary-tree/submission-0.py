# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        cnt = 0
        def dfs(node, cur_max):
            nonlocal cnt
            if not node:
                return
            
            if cur_max <= node.val:
                cnt += 1
            
            if node.left:
                dfs(node.left, max(cur_max, node.val))
            if node.right:
                dfs(node.right, max(cur_max, node.val))
        dfs(root, -float('inf'))
        return cnt