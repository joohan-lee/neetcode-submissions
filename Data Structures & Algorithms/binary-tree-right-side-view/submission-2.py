# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = []

        # BFS and group values at each level. -> return last values at each level.
        q = deque([root])
        while q:
            len_q = len(q)

            curr_level = []
            for i in range(len_q):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            levels.append(curr_level)
        
        return [level[-1] for level in levels]
                
