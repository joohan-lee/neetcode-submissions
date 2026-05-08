# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder에 있는 첫번째 노드는 항상 root.
        in-order의 root기준 앞은 왼쪽 subtree nodes, 뒤는 오른쪽 subtree nodes.
        """
        if not preorder or not inorder:
            return None
        
        # root는 항상 preorder 첫번째.
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # inorder 상 root앞이 모두 left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root