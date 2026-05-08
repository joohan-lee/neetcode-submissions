"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if not node:
                return None
            # 탈출조건: 이미 복사한 node이면 바로 return
            if node in oldToNew:
                return oldToNew[node]

            # 새로 node 만들기
            new_node = Node(node.val)
            oldToNew[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node

        new_root = dfs(node)
        return new_root if node else None