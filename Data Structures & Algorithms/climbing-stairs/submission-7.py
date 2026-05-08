class Solution:
    def climbStairs(self, n: int) -> int:
        """
        풀이1: 지금 i번째 계단에 있어. n번째까지 가는 방법이 몇개지?
                          dfs(0)
                        /      \
                        /        \
                    dfs(1)      dfs(2)
                    /    \       /    \
                    /      \     /      \
                dfs(2)  dfs(3)  dfs(3)  dfs(4)
                /    \    ✓       ✓       ✗
                /      \   
            dfs(3)  dfs(4)
            ✓       ✗

        i == n → 1 (도착 성공 ✓)
        i > n  → 0 (오버슈팅 ✗)
        
        풀이2. 남은 계단 기준 내려오기.
               dfs(3)
                /      \
                /        \
            dfs(2)      dfs(1)
            /    \       /    \
            /      \     /      \
        dfs(1)  dfs(0)  dfs(0)  dfs(-1)
        /    \    ✓       ✓        ✗
    /      \   
dfs(0)  dfs(-1)
    ✓        ✗

remain == 0 → 1 (정확히 소진 ✓)
remain < 0  → 0 (오버슈팅 ✗)
        """
        cache = [-1] * (n)
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)
