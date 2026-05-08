# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, lowerBound, upperBound):
            # Check if lowerBound < node.val < upperBound
            if not node:
                return True
            
            left = isValid(node.left, lowerBound, node.val)
            right = isValid(node.right, node.val, upperBound)
            return lowerBound < node.val < upperBound and left and right

        return isValid(root, float('-inf'), float('inf'))