class Solution:
    def rob(self, nums: List[int]) -> int:
        """
           1         x
          /.\       /
        3   x     2
           /    /
          1     1

        
             2.           x
            / \          / \
           9.  x        7.  x
          /.   / \.         /\
         3. x. 3. x         9 x
            /     /       ...
            1     1
        """
        
        
        memo = [0 for _ in range(len(nums))]

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i]:
                return memo[i]
            
            v1 = nums[i] + dfs(i+2) # rob current house => move to 2 next house

            v2 = dfs(i+1) # not rob current house => move to next house

            memo[i] = max(v1, v2)
            return memo[i]
            
        
        return dfs(0)
