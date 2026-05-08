class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            1           x
          2   x        2  x
        3  x  3  x    3 x 3 x
        [], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]
        '''
        def dfs(level, curr):
            if level == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[level])
            dfs(level+1, curr)
            curr.pop()
            dfs(level+1, curr)
        res = []
        dfs(0, [])
        return res