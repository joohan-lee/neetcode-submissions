# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            # pre-order traversal
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        self.i = 0
        # 풀 때도 여전히 serialize했던 순으로 dfs
        def dfs():
            if vals[self.i] == "N":
                # 방문처리 했으니 +1
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            # 방문처리 했으니 +1
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()

