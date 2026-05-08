# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        p < curr < q
        (p < curr && curr == q) or (curr == p && curr < p)
        위 두 경우가 되는 curr가 lowest ancestor node
        """
        if p.val > q.val:
            p, q = q, p
        res = None
        def dfs(node):
            nonlocal res
            if not node:
                return False
            # print(f'{node.val=}')
            if (p.val < node.val < q.val) or (p.val < node.val and node.val == q.val) or (p.val == node.val and node.val < q.val):
                res = node
                return True
            
            l = dfs(node.left)
            r = dfs(node.right)

            return l or r

        dfs(root)
        return res