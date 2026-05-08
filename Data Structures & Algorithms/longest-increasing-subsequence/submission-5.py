class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
                dfs(0)
                /       \
                dfs(1)     x
            /    \     /     \ 
        dfs(2)     x  dfs(2)  x
        if curr value is larger than previous one, append.
        """
        n = len(nums)
        memo = [-1] * n
        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            res = 1 # base case. 밑에 for loop 안돌 때 하나짜리 LIS. 배열 마지막 요소여서 i+1 == n인 경우 아래 for loop안 돈다.
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    # 더 큰 값 있을때만 방문. 유효한 j만 점프함.
                    res = max(res, 1+ dfs(j))
            memo[i]= res
            return res
        
        return max(dfs(i) for i in range(n))