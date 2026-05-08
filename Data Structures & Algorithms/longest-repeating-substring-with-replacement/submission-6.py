class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window
        """
        현재 슬라이드 윈도우에서 windowLen - max_frequency <= k 이면 그것이 가장 긴 substring
        """

        res = 0
        count = {}

        start = 0
        maxf=0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maxf = max(maxf, count[s[end]])

            # 만약 windowLen - max_frequency 가 k보다 크면 shrink.
            while (end - start + 1) - maxf > k:
                count[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)
        
        return res