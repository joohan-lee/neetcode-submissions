class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            2
           2
          2
         2 x
        2 x
        '''
        def dfs(i, curr):
            curr_sum = sum(curr)
            if curr_sum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr)
            curr.pop()
            dfs(i+1, curr)

        
        res = []
        dfs(0, [])
        return res
