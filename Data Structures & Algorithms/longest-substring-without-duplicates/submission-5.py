class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        start = 0
        res = 0
        for end in range(len(s)):
            while s[end] in charSet:
                # if s[end] is already in window, remove it
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            res = max(res, end - start + 1)
        return res