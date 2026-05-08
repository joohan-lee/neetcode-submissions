class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            dfs(0, 0)
            /         \
        dfs(1, 1)     dfs(1, 0)
        /     \             /     \
    dfs(2, 3) dfs(2,1)    dfs(2,2) dfs(2,0)
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        memo = {} # {(i, acc): bool}
        def dfs(i, acc):
            if i == len(nums):
                return False
            if acc > total / 2:
                return False
            if (i, acc) in memo:
                return memo[(i,acc)]
            
            if acc == total / 2:
                return True
            
            l = dfs(i+1, acc + nums[i])
            r = dfs(i+1, acc)
            memo[(i, acc)] = l or r
            return l or r
        
        return dfs(0, 0)
