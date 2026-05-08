class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
                    []
                /   |        \
               [1]  [2]       [3]
            / |      /|         / |
        [1,2][1,3] [2,1][2,3]  [3,1][3,2]
    /
  [1,2,3] [1,3,2]  [2,1,3] [2,3,1]
        """
        res = []
        def backtrack(i, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in curr:
                    continue
                curr.append(nums[j])
                backtrack(j, curr)
                curr.pop()
        
        backtrack(0, [])
        return res