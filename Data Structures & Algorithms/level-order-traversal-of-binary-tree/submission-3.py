# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, level):
            if not node:
                return
            
            if level < len(res):
                # 이미 방문했던 레벨이면 노드를 해당 레벨에 추가.
                res[level].append(node.val)
            else:
                # 아직 방문하지 못한 노드를 만나면 res에 새로 level 추가.
                # DFS니까 최초 만날때 추가해도 괜찮음.
                res.append([node.val])
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return res
