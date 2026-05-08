class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def dfs(level, curr):
            if level >= len(nums):
                res.add(tuple(curr.copy()))
                return
            
            curr.append(nums[level])
            dfs(level+1, curr)
            curr.pop()
            dfs(level+1, curr)

        res = set()
        dfs(0, [])
        
        return [list(t) for t in res]
