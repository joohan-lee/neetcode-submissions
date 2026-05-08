# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재 노드가 중간 경로가 되는 경우는 아래를 포함해서 위로 path가 이어질 수 있다.
            #       1. 현재 노드만 사용
            #       2. 현재 노드 + left노드
            #       3. 현재 노드 + right노드
            cur_val = max(node.val, node.val + left, node.val + right)

            # 현재 노드가 root가 되는 경우도 있을 수 있다.
            # 이 경우, 현재 노드 + left + right 가 최대일 수 있다.
            max_sum = max(max_sum, cur_val, node.val + left + right)

            return cur_val
        
        dfs(root)
        return max_sum

        
        