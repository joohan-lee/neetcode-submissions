class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        2D DP
        dp[i][a] = coin[i:] 로 만들 수 있는 a의 방법 수. (i부터 끝까지의 코인 종류이므로 dp[n-1]부터 채워나가야함.)
        코인을 [1,3]으로 쓰는 것과 [3,1]로 쓰는 것은 같다. 즉, 코인은 순차적으로만 쓰여야한다.

        dp[i][a] = dp[i+1][a] (현재 코인 안쓰는 경우)
                    + dp[i][a - coins[i]] (현재 코인 쓰는 경우)
        i a 0 1 2 3 4
        0   1 
        1   1
        2   1 0 0 1 0
        3   1 - - - -

        """
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]

        # base case
        # amount==0이면 방법은 1개.
        for i in range(n+1):
            dp[i][0] = 1 

        # 지금은 coins[i:]를 사용해 a를 만든다. 즉, i+1을 통해 i를 계산함으로 역순.
        for i in range(n-1, -1, -1):
            for a in range(amount+1):
                dp[i][a] = dp[i+1][a] # 현재 코인 사용x
                if a >= coins[i]: # 현재 코인 사용 o
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]
