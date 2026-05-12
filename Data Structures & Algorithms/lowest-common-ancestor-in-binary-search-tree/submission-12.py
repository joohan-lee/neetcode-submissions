# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Since it is BST (p < q), p <= curr <= q -> return curr (lowest)
        # p > curr -> move right
        # q < curr -> move left
        if not root:
            return None
        if p.val > q.val:
            p, q = q, p

        if p.val > root.val:
            # 우측만 탐색
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val:
            # 더 큰 값이 root보다 작으면 왼쪽만 보면됨.
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # p <= curr <= q
            return root