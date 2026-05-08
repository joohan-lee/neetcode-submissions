class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # BRUTE FORCE
        res = 0
        for i in range(len(s)):
            count = [0] * 26
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('A')
                count[idx] += 1
                winLen = j - i + 1
                if winLen - max(count) <= k:
                    res = max(res, winLen)
        return res

