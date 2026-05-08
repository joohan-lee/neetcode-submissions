class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 맨 끝 지점을 고정으로 최대값이라고 두고, subsequense 순회하며 큰 값들을 찾는다. O(n^2)
        # dp[i] = 현 지점부터 맨 끝점까지의 LIS
        n = len(nums)
        dp = [1] * (n)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)