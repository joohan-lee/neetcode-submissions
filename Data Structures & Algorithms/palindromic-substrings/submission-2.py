class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Way1. Brute Force
        - 모든 sbustring마다 palindrome인지 체크.
        
        Way2. Bottom up DP
          a a a
        a T T T
        a   T T
        a     T
            => True의 개수 세기.
        dp(i,j) = dp(i+1, j-1) == True and s[i] == s[j]
        
        Way3. Two pointers
        - "Palindrome + substring" 보이면 → 중심 확장부터 떠올려

        Way4. Top down DP (Palindrome에서 잘 안쓰긴 함)
        """
        # top-down dp  (palindrome은 어짜피 모든 substring을 봐야해서 top down dp로 잘 안풀긴하지만, 풀면 아래처럼 가능.)
        # s[i:j]가 palindrome인지를 memoization하기 때문에 결과적으로 한번씩만 계산해서 Brute force와 달리 O(n^2) solution 가능.
        n = len(s)
        memo = [[None] * n for _ in range(n)]
        def isPalin(i, j):
            if i >= j:
                memo[i][j] = 1
                return 1
            if memo[i][j] != None:
                return memo[i][j]
            if s[i] != s[j]:
                memo[i][j] = 0
                return 0
            memo[i][j] = isPalin(i+1, j-1) 
            return memo[i][j]
        
        res = 0
        for i in range(n):
            for j in range(i, n):
                if isPalin(i, j):
                    res += 1
        return res