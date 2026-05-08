class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        min_w = len(s) + 1
        res = ""
        t_chars = {}
        for ch in t:
            t_chars[ch] = t_chars.get(ch, 0) + 1
        
        window_counts = {}
        have, need = 0, len(t_chars)
        
        while end < len(s):
            new_letter = s[end]
            window_counts[new_letter] = window_counts.get(new_letter, 0) + 1

            # t와 동일하게 개수까지 다 채워진 알파벳은 have로 침.
            if new_letter in t and window_counts[new_letter] == t_chars[new_letter]:
                have += 1
                
            # If all characters are included, update min_w and shrink
            while have == need:
                if min_w > (end - start + 1):
                    min_w = end - start + 1
                    res = s[start:end+1]

                start_letter = s[start]
                window_counts[start_letter] -= 1
                if start_letter in t_chars and window_counts[start_letter] < t_chars[start_letter]:
                    have -= 1
                    
                start += 1
            end += 1
        
        return res

