# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            curr = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            curr_max = max(curr, left+curr, right+curr) # 위로 전달할 때는 양쪽 방향을 포함해서는 안됨.
            res = max(res, curr_max, left+right+curr) # 전역 최대일때만 양방향 함께 고려.
            return curr_max

        dfs(root)
        return res
