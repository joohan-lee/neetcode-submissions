class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 0
        last_idx = defaultdict(int)
        res = 0
        while r < len(s):
            if s[r] in last_idx:
                l = max(last_idx[s[r]] + 1, l)
            last_idx[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res



