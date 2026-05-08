class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
            a       aa      aab
          a  ab    b       
         b

        Time complexity는 길이가 n개인 문자열일 때, 각 문자열을 자를지 마를지 구분할 구분 선은
        각 문자 사이이므로 총 (n-1)개이고, 각 구분 선에서 자를 수도 안 자를수도 있다. O(2^(n-1))
        또, 자른 후에 각 substring의 palindrome여부 확인하므로, O(n)
        Thus, total time complexity = O(n * 2^(n-1))
        space complexity = O(n)
        
        '''
        def _is_palindrome(s):
            if not s: return False

            l, r = 0, len(s) - 1
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(i, curr):
            # print(f'{i=}, {curr=}')
            if i == len(s):
                res.append(curr.copy())
                return
            # 한번에 묶어서 뒤에 붙이므로 딱 갯수가 맞지 않을 떄는 res에 저장 안함.
            if i > len(s):
                return
            
            for j in range(len(s)):
                if not _is_palindrome(s[i:i+j+1]):
                    continue
                curr.append(''.join(s[i:i+j+1])) # i로부터 j개를 넣는다.
                backtrack(i+j+1, curr)
                curr.pop() # 다음 j를 dfs하기 위해 이전 j개는 pop해준다.
        
        res = []
        backtrack(0, [])
        return res
