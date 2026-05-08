class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j # need insert operations as many as remaining word2 chars times
            if j >= len(word2):
                return len(word1) - i # need delete operations as many as remaining word1 chars times
            if (i,j) in dp:
                return dp[(i,j)]

            res = float('inf')
            if word1[i] == word2[j]:
                # Matched. both i, j increment. (no operation req.)
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]
            else:
                # Insert
                res = min(res, dfs(i, j+1) + 1)
                # Delete
                res = min(res, dfs(i+1, j) + 1)
                # Replace
                res = min(res, dfs(i+1, j+1) + 1)
            dp[(i,j)] = res
            return res
        
        return dfs(0, 0)
