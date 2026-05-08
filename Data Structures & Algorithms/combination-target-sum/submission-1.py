class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr):
            if sum(curr) > target:
                return
            
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j, curr)
                curr.pop()
        
        backtrack(0, [])
        return res
            
