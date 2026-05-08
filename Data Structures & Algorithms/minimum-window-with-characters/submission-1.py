class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        
        def isIncluded(mp1, mp2):
            # Check if mp2 is inclueded in mp1
            for k, v in mp2.items():
                if k not in mp1 or mp1[k] < mp2[k]:
                    return False
            
            return True
        window = {}
        min_len = float('inf')
        start = 0
        res = ""
        # print(f'{count=}')
        for end in range(len(s)):
            window[s[end]] = window.get(s[end], 0) + 1

            while start <= end and isIncluded(window, count):
                # print(f'{window=}')
                # print(f'{start=}, {end=}')
                if min_len > (end - start + 1): 
                    res = s[start:end+1]
                    min_len = (end-start+1)
                window[s[start]] -= 1
                start += 1
        
        return res

