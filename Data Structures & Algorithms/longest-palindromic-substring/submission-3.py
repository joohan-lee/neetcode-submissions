class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        dp[i, j] = substring [i,j] is a palindrome or not. (i<=j)
        dp[i, j] = True, if dp[i+1, j-1] == True and s[i] == s[j]
                   False, otherwise.
        dp[i, i] = True
        dp[i, i+1] = True, if s[i] == s[i+1], False, otherwise
        "babad"
          0 1 2 3 4(j)
        0 T F T F F
        1   T F T F
        2.    T F F
        3.      T F
        4         T
        (i)

        """
        N = len(s)
        dp = [[False] * N for _ in range(N)]

        max_str = (0, 0)
        for i in range(N):
            dp[i][i] = True
            if i+1 < N:
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
                    max_str = (i, i+1)
        
        for k in range(2, N):
            for r in range(N):
                c = r + k
                if 0<= r < N and 0<=c < N and dp[r+1][c-1] == True and s[r] == s[c]:
                    dp[r][c] = True
                    if (c-r+1) > (max_str[1] - max_str[0]):
                        max_str = (r, c)
        
        return s[max_str[0]:max_str[1]+1]
