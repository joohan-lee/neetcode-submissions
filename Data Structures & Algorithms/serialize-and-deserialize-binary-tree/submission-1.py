# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        if vals[0] == "N":
            return None
        
        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)
        
        idx = 1
        while q:
            node = q.popleft()
            if vals[idx] != "N":
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx += 1
            if vals[idx] != "N":
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx += 1
        return root


    
        
    