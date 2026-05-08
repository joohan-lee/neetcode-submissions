class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []
        def _is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(i, curr):
            """
            i: current idx at s
            curr: substrings so far
            """
            if i == len(s):
                res.append(curr.copy())
                return
            
            if i > len(s):
                return
            
            for j in range(len(s)-i):
                if not _is_palindrome(s[i:i+j+1]):
                    continue
                curr.append(''.join(s[i:i+j+1]))
                backtrack(i+j+1, curr)
                curr.pop()
        backtrack(0, [])
        return res