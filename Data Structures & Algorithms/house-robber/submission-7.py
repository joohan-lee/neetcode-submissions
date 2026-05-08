class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Top Down
            dfs(0)
           /(x)    \(o)
        dfs(1)    dfs(2)
      /     \       /     \
  dfs(2)  dfs(3)  dfs(3)  dfs(4)
  /   \
dfs(3)  dfs(4)
/     \
dfs(4) dfs(5)
        """
        cache = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            rob = nums[i] + dfs(i+2)
            no_rob = dfs(i+1)

            cache[i] = max(rob, no_rob)
            return cache[i]
        
        return dfs(0)