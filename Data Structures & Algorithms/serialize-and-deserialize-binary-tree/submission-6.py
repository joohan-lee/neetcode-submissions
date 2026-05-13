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
            return ""
        res = []
        
        q=deque([root])
        res.append(str(root.val))
        while q:
            node = q.popleft()
            
            if node.left:
                res.append(str(node.left.val))
                q.append(node.left)
            else:
                res.append("N")
            if node.right:
                res.append(str(node.right.val))
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        idx = 0
        vals = data.split(',')
        # print(f'{vals=}')
        
        q = deque()
        root = TreeNode(vals[idx])
        q.append(root)
        idx += 1

        # bfs (level-order traversal)
        while q:
            node = q.popleft()
            if vals[idx] != "N":
                left_node = TreeNode(vals[idx])
                node.left = left_node
                q.append(left_node)
            else:
                node.left = None
            idx += 1

            if vals[idx] != "N":
                right_node = TreeNode(vals[idx])
                node.right = right_node
                q.append(right_node)
            else:
                node.right = None
            idx += 1
        return root
