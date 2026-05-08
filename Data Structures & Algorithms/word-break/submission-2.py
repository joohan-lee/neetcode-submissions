class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            leet
        leet code
        """
        wordSet = set(wordDict)
        memo = [None] * len(s)
        def dfs(start):
            if start > len(s):
                return False
            if start == len(s):
                return True
            if memo[start] is not None:
                return memo[start]
            
            for end in range(start, len(s)):
                if s[start:end+1] in wordSet and dfs(end+1):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        
        return dfs(0)
