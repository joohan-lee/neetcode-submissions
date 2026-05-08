class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        d(0) = 1 
        d(i) = max(1 + d(j)) for j < i and nums[j] < nums[i]
        '''
        n = len(nums)
        dp = [0] * (n)
        dp[0] = 1
        res = 0
        for i in range(1, n):
            dp[i] = max([1 + dp[j] for j in range(i) if nums[j] < nums[i]] + [1])
        # print(f'{dp=}')
        return max(dp)
