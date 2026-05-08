class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [1,3,4,5] / 7
        5+1+1=7, 3+4=7

              1
          /.     \
        1 3 4 5   1 3 4 5
       
        """
        n = len(coins)
        opt = [amount+1] * (amount+1)

        # Base case
        opt[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    opt[a] = min(opt[a-c] + 1, opt[a])
        
        return opt[amount] if opt[amount] != amount+1 else -1