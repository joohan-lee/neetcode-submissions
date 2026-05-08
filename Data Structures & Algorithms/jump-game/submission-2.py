class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        [1,2,0,1,0]
            0
          1
         2 3 
        x   '4'
        [2,3,1,1,4]
            0
        1.      2
      2 3 '4'    3
      3 '4'       '4'
        """
        # DP (Bottom-up)
        # dp[i] = whether we can jump to the end at i.
        n = len(nums)
        dp = [False] * n

        dp[-1] = True

        for i in range(n-2, -1, -1):
            end = min(i + nums[i], len(nums) - 1)
            for j in range(i, end + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

