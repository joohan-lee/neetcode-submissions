class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if window does not include t, expand
        # if window already includes t, shrink.
        # find the min window
        res = float('inf')
        res_str = ""
        start = 0
        
        target = defaultdict(int)
        for ch in t:
            target[ch] += 1
        
        def is_included(substr: dict):
            # O(52) = O(1)
            for ch, cnt in target.items():
                if substr[ch] < cnt:
                    return False
            return True
        
        window = defaultdict(int)
        for end in range(len(s)):
            window[s[end]] += 1
            while is_included(window):
                if res > end - start + 1:
                    res = end - start + 1
                    res_str = s[start:end+1]
                window[s[start]] -= 1
                start += 1
            
        return res_str