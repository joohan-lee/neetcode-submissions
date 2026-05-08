class Solution:
    def integerBreak(self, n: int) -> int:
#         """
#              dfs(4)
#         /       |         \
#     1*dfs(3)  2*dfs(2)  3*dfs(1)
#       /  \         
# 1*dfs(2) 2*dfs(1)
#         """
        dp = {}
        def dfs(i):
            if i == 1:
                return 1
            if i in dp:
                return dp[i]
            
            res = 0
            for j in range(1, i):
                res = max(res, j * max(i-j,dfs(i-j))) # i-j가 2 일때는, dfs(2)로 쪼개기보다 2를 그냥 쓰는게 더 큼.
                            # 안쪼갬,  안쪼갬, 더 쪼갬
                # print(f'{i=},{j=},{res=}')
            dp[i] = res
            return res
        
        return dfs(n)