class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            1           x
          2   x        2  x
        3  x  3  x    3 x 3 x
         
        [], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]
        '''
        '''
            1        x
          2   x    2  x
        3  x 3  x 3 x 3 x
        -
        
        level=0, curr= [1]
        level=1, curr= [1,2]
        level=2, curr= [1,2,3]
        level=3, res=[[1,2,3]] -> return
        level=2, curr= [1,2]
        level=3, res=[[1,2,3], [1,2]]

        '''
        def dfs(level, curr: List[int]):
            print(f'{level=}, {curr=}')
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