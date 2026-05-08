# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder: 
            - first elem is root
            - second elem is root of left subtree
            - preorder[len(left_subtree)+1] is root of right subtree
        inorder: 
            - left-side of root is left subtree, the other -> right subtree.
            - can get the length of left subtree, right subtree
            - first elem is 

        """
        if not preorder:
            return None
        
        root_val = preorder[0]
        node = TreeNode(val=root_val)

        left_length = inorder.index(root_val)
        right_length = len(inorder) - left_length - 1

        node.left = self.buildTree(preorder[1:1+left_length], inorder[:left_length+1]) # traverse left
        node.right = self.buildTree(preorder[1+left_length:], inorder[left_length+1:]) # traverse right

        return node