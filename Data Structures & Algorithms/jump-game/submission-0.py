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
        # Backtracking (Recursion) solution (TLE)

        def dfs(i):
            if i >= len(nums) - 1:
                return True
            
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    return True
            
            return False
        
        return dfs(0)

