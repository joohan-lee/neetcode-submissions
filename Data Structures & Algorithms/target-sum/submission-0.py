class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #
    #         +2(0)             -2(0)
    #       /     \
    #      +2(1)   -2(1)
    #     /   \     /   \
    #  +2(2)  -2(2)+2(2)  -2(2)
    #   |      |     |      |
    #   6      2     2      -2
    #   0      1     1
    #   dfs(i, curr_sum) -> nums[:i+1] 까지로 curr_sum을 만들 수 있는 방법 수.
        

        dp = {} # {(i, curr_sum): # of ways}
        def dfs(i, curr_sum):
            if i == len(nums) and curr_sum == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            # print(f'{i=}, {curr_sum=}')
            res = dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])
            dp[(i, curr_sum)] = res
            return res
        
        return dfs(0, 0)