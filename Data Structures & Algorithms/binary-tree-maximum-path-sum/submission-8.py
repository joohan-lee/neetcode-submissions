# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node.val
            cur_max = max(left + cur, right + cur, cur) # can escalate to the above caller as a sub-path
            res = max(left + cur + right, cur_max, res)
            # print(f'{cur=}, {left=}, {right=}, {cur_max=}, {res=}')
            return cur_max
        
        dfs(root)
        return res