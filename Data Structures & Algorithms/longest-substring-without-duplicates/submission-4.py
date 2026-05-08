class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        res = 0
        start = 0
        for end in range(len(s)):
            while start <= end and s[end] in substr:
                substr.remove(s[start])
                start += 1
            substr.add(s[end])
            res = max(res, len(substr))
        
        return res
