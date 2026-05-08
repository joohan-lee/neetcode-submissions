class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Bottom Up (뒤에서 부터 해보기)
        # dp[i] = whether we can reach the end at i

        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            end = min(i + nums[i], len(nums) - 1)
            for j in range(i+1, end + 1):
                # If we have a point that can reach after i, dp[i] = True
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]