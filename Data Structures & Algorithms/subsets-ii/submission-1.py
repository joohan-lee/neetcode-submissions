class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        2. Backtracking (Pick / Not Pick)풀이
                1           x
             1    x    1(SKIP) x
           2  x  2 x          2  x
     [112],[11],[12],[1],    [2] []

        
        '''
        nums.sort()

        def dfs(level, curr):
            print(f'{level=}, {curr=}')
            if level >= len(nums):
                res.append(curr.copy())
                print(f'added {curr}')
                return
            
            curr.append(nums[level])
            dfs(level+1, curr)
            a = curr.pop()
            print(f'popped {a}')

            # 앞 인덱스에서 뺀 값이 다음에 중복으로 되어 진행하지 않도록 앞 값과 다를 떄까지 skip.
            while level + 1 < len(nums) and nums[level] == nums[level+1]:
                print(f'Skip! {level=}, {nums[level]} == {nums[level+1]}')
                level += 1
            dfs(level+1, curr)

        res = []
        dfs(0, [])
        
        return res
