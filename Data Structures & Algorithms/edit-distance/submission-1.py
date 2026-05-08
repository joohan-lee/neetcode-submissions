class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        0. 각 스텝에서 무엇을 할 수 있는지를 바탕으로 recursion decision tree그려보기.
        1. 상태 정의
        dfs(i,j) => Operations to change word1[i:] into word2[j:] (word1[i:]를 word2[j:]로 바꾸는데 필요한 연산 수)
        2. 베이스 케이스
        더 이상 줄일 수 없는 상태
        3. 전이 (transition)
        현재 상태에서 어떤 선택지가 있고, 각 선택이 상태를 어떻게 변화시키나?
        4. memoization 추가

            dfs(0,0)
                | word1[0] == word2[0] (같으면 그대로 둘 다 넘어감)
            dfs(1,1)
                | word1[1] == word2[1]
            dfs(2,2)
                | word1[2] == word2[2]
            dfs(3,3)
          /delete |insert    \replace   (다르면 연산 하나를 하여 세가지 경우로 나뉨)
    dfs(4,3)    dfs(3,4)  dfs(4,4)

        """
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
