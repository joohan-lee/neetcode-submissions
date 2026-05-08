class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr):
            nonlocal target
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if sum(curr) > target:
                return
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j, curr)
                curr.pop()

        dfs(0, [])
        return res