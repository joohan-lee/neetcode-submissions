class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        s3의 k위치는 s1의 i 글자에서 온 것일수도 있고, s2의 j 글자에서 온 것일수도.
        즉, s1의 i상태, s2의 j상태가 있으면 s3의 i+j 상태를 만들 수 있어 2D DP 가능.
        s1="ab" s2="ac" s3="aabc"
            (0,0)
            s3[0]='a'
            /       \
        (1,0)       (0,1)
        s1[1]=a     s2[1]=a
        
        """
        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
                
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    dp[(i,j)] = True
                    return dp[(i,j)]
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    dp[(i,j)] = True
                    return dp[(i,j)]
            
            dp[(i,j)] = False
            return False
        
        return dfs(0,0,0)
