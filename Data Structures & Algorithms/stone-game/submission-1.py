class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        O(1) solution: sum이 odd이므로 sum(odd idx) != sum(even idx)이므로
        alice가 둘 중 하나의 sum이 되도록 optimal하게 고르면 무조건 이긴다.
        그리고, 그렇게 고르는 방법은 무조건 존재하니 alice가 늘 이긴다.

        다만, sum이 odd라는 보장이 없으면? 이라는 follow up 질문이 있다면
        각 turn에서의 경우의 수를 따져봐야하고, 각 턴에서 alice는 l, r 중 하나를 고르므로
        O(2^n)으로 해결된다. 다만, DP로 O(n^2)로 줄일 수 있음.

        O(n^2) solution: DP.
        dp[l,r] = piles[l:r]로 만들 수 있는 alice의 최대 합.
        아래 tree에서 bob turn에서는 alice가 고르지 않으면 된다.
        [1,2,3,1]
        Each turn, Alice takes left or right. then alice's total is
                  0
            /l         \r
alice      1           1
       /1   \3           /0  \2
bob   1     1          1    1
     /2\3
    3  1

                dfs(l,r)
                /       \
            dfs(l+1,r)  dfs(l, r-1)
        """
        
        dp = {} # (l,r): alice max total
        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            is_alice_turn = (r-l) % 2 == 0 # alice turn
            left = piles[l] if is_alice_turn else 0
            right = piles[r] if is_alice_turn else 0

            dp[(l,r)] = max(dfs(l+1, r) + left, dfs(l, r-1) + right)
            return dp[(l,r)]
        
        alice = dfs(0, len(piles) - 1)
        return alice > sum(piles) - alice
