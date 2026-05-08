class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.add(tuple(sorted(curr.copy())))
            if i >= len(candidates) or curr_sum > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, curr_sum + candidates[i])
            curr.pop()
            dfs(i+1, curr, curr_sum)

        res=set()
        dfs(0, [], 0)
        
        return [list(t) for t in res]