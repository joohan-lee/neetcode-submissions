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
        
        def dfs(node):
            
            if not node:
                return False
            # print(f'{node.val=}')
            if (p.val < node.val < q.val) or (p.val < node.val and node.val == q.val) or (p.val == node.val and node.val < q.val):
                return node
            
            if q.val < node.val:
                return dfs(node.left)
            if p.val > node.val:
                return dfs(node.right)


        return dfs(root)