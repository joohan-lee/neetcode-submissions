import functools
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
        res = 0 # max amount of money
        visited = set()
        @functools.cache
        def dfs(i, curr):
            nonlocal res
            if i in visited:
                return
            if i >= len(nums):
                res = max(res, curr)
                return
            
            visited.add(i)
            dfs(i+2, curr + nums[i]) # rob current house => move to 2 next house

            visited.remove(i)
            dfs(i+1, curr) # not rob current house => move to next house
            
        
        dfs(0, 0)

        return res
