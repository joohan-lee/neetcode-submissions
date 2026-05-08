# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        cur = self.isValid(root.left, root.val, True) and self.isValid(root.right, root.val, False)
        return cur and self.isValidBST(root.left) and self.isValidBST(root.right)
        
    
    def isValid(self, node, limit, smaller:bool):
        if not node:
            return True
        
        if smaller:
            if node.val >= limit:
                return False
        else:
            if node.val <= limit:
                return False
        
        return self.isValid(node.left, limit, smaller) and self.isValid(node.right, limit, smaller)


        
        