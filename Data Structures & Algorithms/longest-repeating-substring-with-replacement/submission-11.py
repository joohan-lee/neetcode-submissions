class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window: one character with k replacement
        # {char: cnt}
        # expand: cnt++ or new char using replacement
        # shrink: cnt-- or remove char when it becomes zero cnt
        
        start = 0
        maxf = 0
        res = 0
        counter = {}

        for end in range(len(s)):
            counter[s[end]] = counter.get(s[end], 0) + 1 # 현재 윈도우 char frequency.

            # (현재 윈도우 크기) - (최대 빈도수) > k이면 k 이상 replacement 필요한것이니 shrink.
            # upper case만 고려하니 max frequency 구하는 것은 O(26)=O(1)
            while ((end - start + 1) - max(counter.values())) > k:
                counter[s[start]] -= 1
                start += 1
            res = max(res, (end-start+1))
        return res