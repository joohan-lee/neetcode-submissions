class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [100000] * n
        dp[-1] = 0

        for i in range(n-2, -1, -1):
            end = min(n-1, i + nums[i])
            for j in range(i+1, end+1):
                dp[i] = min(dp[i], 1+dp[j])
        
        return dp[0]