class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 현재 window에서 가장 frequent한 character 구하는 것은 알파벳 수는 항상 26이므로 O(1).

        counter = {}
        start = 0
        maxf = 0
        res = 0

        # Expanding Window
        for end in range(len(s)):
            counter[s[end]] = counter.get(s[end], 0) + 1
            # maxf = max(maxf, counter[s[end]]) # max frequency at current window

            # Shrink window
            while ((end - start + 1) - max(counter.values())) > k:
                counter[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res