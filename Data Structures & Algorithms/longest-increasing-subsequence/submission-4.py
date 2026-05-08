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
        memo = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i,prev)]

            res = dfs(i+1, prev) # 현재 값 선택 x
            if nums[i] > prev:
                # 현재 값 선택 가능할 때만
                res = max(dfs(i+1, nums[i]) + 1, res)
            memo[(i,prev)]= res
            return memo[(i,prev)]

        
        return dfs(0, float('-inf'))