class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # to avoid visiting duplicates

        res = []
        def backtrack(i, curr):
            total = sum(curr)
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                backtrack(j+1, curr)
                curr.pop()
        
        backtrack(0, [])
        return res