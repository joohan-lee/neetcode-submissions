class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            1       2       3
          2  3
         3   2

        '''
        def dfs(idx, curr):
            if idx >= len(nums):
                res.append(curr.copy())
                return
            
            curr_set = set(curr)
            remainings = [num for num in nums if num not in curr_set]
            for n in remainings:
                curr.append(n)
                dfs(idx+1, curr)
                curr.pop()

        res = []
        dfs(0, [])
        return res