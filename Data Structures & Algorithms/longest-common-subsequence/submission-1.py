class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 is shorter.
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        memo = defaultdict(int)
        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1) # 매칭되었으면 무조건 둘다 건너가야함. 아니면 j남겨두고 i만 가면서 j와 매칭되는걸 두번 찾을수도 있음.    
            else:
                memo[(i,j)] = max(dfs(i,j+1), dfs(i+1,j)) # # i미포함/j포함, i포함/j미포함
            return memo[(i,j)]
        
        return dfs(0,0)
        