class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            dfs(0)                dfs(1)
           /      \            /(1안털고) \(1털고3으로)
        dfs(1)   dfs(2)      dfs(2)  dfs(3)
        털어온 path를 기록하면, 끝에서 0을 포함하는지 아닌지 체크 가능.
        혹은 단순히 0을 포함하는지만 체크해도 되겠다.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i, flag):
            """
            i: current house
            flag: whether the first house was robbed
            """
            if i >= len(nums):
                return 0
            if i == len(nums) - 1 and flag:
                # If the first house was robbed, no need to check the last house.
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            rob = nums[i] + dfs(i+2, flag)
            no_rob = dfs(i+1, flag)

            memo[i][flag] = max(rob, no_rob)

            return memo[i][flag]
        
        return max(dfs(0, True), dfs(1, False))
            
