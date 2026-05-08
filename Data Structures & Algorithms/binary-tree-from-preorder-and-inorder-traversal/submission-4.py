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
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(l, r):
            # l, r은 inorder의 idx.
            if l > r:
                # 빈 서브트리. (노드 0개)를 의미.
                return None

            root_val = preorder[self.pre_idx] # 
            self.pre_idx += 1 # preorder traversal하므로 그 다음 값이 항상 root node (다음 left subtree 탐색하니까 그의 root)
            
            node = TreeNode(root_val)
            mid = indices[root_val]

            # preorder다음 elem이 왼쪽 서브트리의 root이니 왼쪽 먼저! 
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid+1, r)

            return node
        return dfs(0, len(inorder) -1)