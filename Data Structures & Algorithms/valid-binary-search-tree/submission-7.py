# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, cur_min, cur_max):
            if not node:
                return True
            if not (cur_min < node.val < cur_max):
                return False
            return dfs(node.left, cur_min, node.val) and dfs(node.right, node.val, cur_max)
        
        return dfs(root, float('-inf'), float('inf'))