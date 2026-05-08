class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
            1       2       3
         /  | \
        1  2  3
      /| \ 
     1
    /
    1
   (1)

        dfs(i, remaining)
        """
        dp = defaultdict(int)
        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            curr_total = 0
            for j in range(i, len(coins)):
                curr_total += dfs(j, remaining - coins[j])
            
            dp[(i, remaining)] = curr_total
            return curr_total
        
        return dfs(0, amount)