# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                serialized.append("N")
                return
            # pre-order traversal
            serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        idx = 0
        def dfs() -> Optional[TreeNode]:
            nonlocal idx
            if vals[idx] == "N":
                idx += 1 # N 읽었으니 idx 증가
                return None
            root = TreeNode(int(vals[idx]))
            idx += 1 # val 읽었으니 idx 증가
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        