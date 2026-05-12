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
        val_idx_mp = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            # inorder 범위가 비면 서브트리 없음
            if left > right:
                return None
            # preorder에서 다음 root 꺼내고 앞으로만 진행.
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1 # 그 다음 값이 항상 왼쪽 subtree root. 그리고 항상 left subtree부터 방문하므로 다음 root가 됨.
            
            mid = val_idx_mp[root.val] # inorder에서 root위치 => 좌/우 서브트리 경계

            root.left  = dfs(left, mid-1) # left subtree에 대해 진행.
            root.right = dfs(mid + 1, right)
            
            return root
        return dfs(0, len(inorder) - 1)
        