class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            2       x
          /  \
        2     x
      /   \
    2      x
    /\
    2   x
   /\  / \
  2  x 3  x
        """
        
        res = []
        def backtrack(i, curr):
            total = sum(curr)
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()
            backtrack(i+1, curr)
        
        backtrack(0, [])
        return res


            