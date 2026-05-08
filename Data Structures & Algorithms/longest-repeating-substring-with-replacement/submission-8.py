class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        
        """
        ABCDEFGGG
        GABCAGFHKISSG, k=2
        G is the most frequent, but answer is "ABCA" -> "AAAA", 4.

        start기준으로 다른게 k만큼 있을 때까지만 end 진행.


        ABCBAA -> 
        """
        counter = {} #[0] * 26 # A-Z
        start = 0
        res = 0
        for end in range(len(s)):
            counter[s[end]] = counter.get(s[end], 0) + 1
            if (end - start + 1) - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1
            res = max(res, (end - start + 1))
        
        return res