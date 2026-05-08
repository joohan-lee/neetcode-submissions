class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [1,2,2,4,5,6,9]
        """
        candidates.sort()
        
        res = set()
        def backtrack(i, curr):
            if sum(curr) == target:
                res.add(tuple(curr))
                return
            
            if sum(curr) > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
        
        backtrack(0, [])
        return [list(t) for t in res]