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
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # base case
        for i in range(n):
            dp[i][i] = 1
            if i+1 < n:
                dp[i][i+1] = 1 if s[i]==s[i+1] else 0

        # (0,1)->(1,2)
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                dp[i][j] = 1 if dp[i+1][j-1] and s[i] == s[j] else 0

        # Generator! which does not allocate memory, but just create and remove every iteration
        """
        # List comprehension → 리스트 전체가 메모리에
        squares_list = [i ** 2 for i in range(1000000)]  # 100만 개 메모리에 올림

        # Generator expression → 하나씩 생성
        squares_gen = (i ** 2 for i in range(1000000))   # 거의 메모리 안 씀

        # ✅ generator → O(1) 공간
        - sum()이 generator에서 값을 하나 꺼내고 → 더하고 → 다음 값 꺼내고 → 더하고... 를 반복하니까, 동시에 하나의 값만 메모리에 존재해.
        - range() 자체도 사실 generator와 비슷한 lazy evaluation 객체야
        - generator는 한 번만 순회 가능 (리스트처럼 다시 돌릴 수 없음)
        """
        return sum(dp[i][j] for i in range(n) for j in range(n)) 
        