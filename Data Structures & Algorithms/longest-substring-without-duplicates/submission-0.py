class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        res = 0        
        for i in range(len(s)):
            visit = set()
            visit.add(s[i])
            curr = 1
            for j in range(i+1, len(s)):
                if s[j] in visit:
                    break
                visit.add(s[j])
                curr += 1
            res = max(res, curr)
        return res
