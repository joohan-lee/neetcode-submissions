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
        # Greedy
        n = len(nums)
        goal = len(nums) - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0