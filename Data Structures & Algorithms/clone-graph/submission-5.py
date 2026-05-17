"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        1. copy node
        2. traverse neighbors
        3. connect nodes (postorder)
        """
        if not node:
            return None

        oldToNew = {} # track all created nodes
        def dfs(node):
            if node in oldToNew:
                # if already created, early return. 아니면 cycle있을 때 무한루프.
                # 1-2
                # | |
                # 3-4
                return oldToNew[node]
            
            new_node = Node(node.val)
            oldToNew[node] = new_node
            for nei in node.neighbors:
                new_nei = dfs(nei)
                new_node.neighbors.append(new_nei) # new_node -> new_nei
                # new_nei.neighbors.append(new_node) # new_nei -> new_node
            
            return new_node
        
        return dfs(node)