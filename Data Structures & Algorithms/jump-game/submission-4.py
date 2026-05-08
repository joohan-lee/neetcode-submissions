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
        # memo[i] = whether we can jump to the end at i.
        cache = {}
        def dfs(i):
            if i >= len(nums)-1:
                return True
            if i in cache:
                return cache[i]
            if nums[i] == 0:
                return False
            
            for k in range(1, nums[i]+1):
                a = dfs(i+k)
                if a:
                    cache[i] = a
                    return cache[i]
            cache[i] = False
            return False
        return dfs(0)
