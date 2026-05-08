class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # SLIDING WINDOW
        res = 0
        charSet = set(s)

        for ch in charSet:
            count = l = 0
            for r in range(len(s)):
                # r을 늘려가며, 즉 윈도우 사이즈를 늘려가며 현재 캐릭터 수 카운트.
                if s[r] == ch:
                    count += 1
                
                # 현재 윈도우에서 현재 캐릭터가 아닌 것의 개수가 k개가 넘어가면,
                # l을 다음 현재 캐릭터 ch가 아닌 곳으로 이동(윈도우 사이즈를 줄임). 이 과정에서 당연히 count 빼줌.
                windowSize = r - l + 1
                while windowSize - count > k:
                    if s[l] == ch:
                        count -= 1
                    # l 이동.
                    l += 1
                    windowSize = r - l + 1
                res = max(res, windowSize)

        return res