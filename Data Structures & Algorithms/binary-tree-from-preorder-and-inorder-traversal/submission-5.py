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

        Preorder가 "무엇을" 만들지 결정하고, Inorder가 "언제까지" 만들지 결정한다.
        preorder: [3, 9, 20, 15, 7]  ← 순차적으로 하나씩 꺼내서 root로
                     →  →  →   →  →

        inorder:  [9, 3, 15, 20, 7]  ← 범위 [l, r]로 "이 서브트리에 몇 개?"
                    └─┴──┴───┴──┘
        pre_idx는 절대 뒤로 안 가고 앞으로만 진행
        [l, r] 범위가 쪼개지면서 재귀 깊이/횟수 조절
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left_length = inorder.index(root.val)
        root.left  = self.buildTree(preorder[1:left_length+1], inorder[:left_length])
        root.right = self.buildTree(preorder[left_length+1:], inorder[left_length+1:])
        
        return root
        