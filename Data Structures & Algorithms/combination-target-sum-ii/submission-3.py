class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [1,2,2,4,5,6,9]
        """
        candidates.sort()
        
        res = []
        def backtrack(i, curr):
            # print(f'{i=}, {curr=}')
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if sum(curr) > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i+1, curr)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr)
        
        backtrack(0, [])
        return res