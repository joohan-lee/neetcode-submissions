"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        def getCopy(node):
            if node == None:
                return None
            # if node in hash_map:
            #     return hash_map[node]
            
            copy = Node(node.val)
            hash_map[node] = copy
            copy.next = getCopy(node.next)
            copy.random = hash_map.get(node.random, None)

            return copy
        getCopy(head)
        return hash_map.get(head, None)