class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # SLIDING WINDOW O(len(s))
        
        l, r = 0, 0
        count = [0] * 26
        res = 0
        maxf = 0
        while r < len(s):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            # windowSize = r - l + 1
            maxf = max(maxf, count[idx])
            while (r - l + 1) - maxf > k:
                count[ord(s[l]) - ord('A')]-= 1
                l += 1
                
            res= max(res, r - l + 1)

            r += 1

        return res