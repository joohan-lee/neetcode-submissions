# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val =0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            raise ValueError
        # while bfs,
        # if root is the same, compare two trees
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == subRoot.val and self.sameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
                
    
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not (p and q and p.val == q.val):
            return False
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)