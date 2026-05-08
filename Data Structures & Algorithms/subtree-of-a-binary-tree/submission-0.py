# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if (not p and q) or (p and not q):
                return False
            if not p and not q:
                return True
            
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right and p.val == q.val
        
        def dfs(node):
            if not node:
                return False
            isSame = False
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    isSame = True
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right or isSame
            


        return dfs(root)