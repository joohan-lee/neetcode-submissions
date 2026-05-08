"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(curr):
            if not curr:
                return None
            if not curr.neighbors:
                return Node(curr.val)
            
            new_node = Node(curr.val)
            visited[new_node.val] = new_node
            for nei in curr.neighbors:
                if nei.val not in visited:
                    new_node.neighbors.append(dfs(nei))
                else:
                    new_node.neighbors.append(visited[nei.val])
            
            return new_node

        new_root = dfs(node)
        return new_root