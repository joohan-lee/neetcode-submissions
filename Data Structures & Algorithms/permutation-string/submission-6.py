class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Way 1. sort & check inclusion
        # Way 2. sliding window

        # Expand window if current window has characters in s1
        # Shrink if a character not in s1 found.
        #   - can start from the end of window again because all previous are not valid.
    
        counter_s1 = {}
        for ch in s1:
            counter_s1[ch] = counter_s1.get(ch, 0) + 1
        
        start = 0
        counter_s2 = {}
        for end in range(len(s2)):
            counter_s2[s2[end]] = counter_s2.get(s2[end], 0) + 1
            if counter_s1 == counter_s2:
                # O(26)
                return True
            
            if (end - start + 1) >= len(s1):
                counter_s2[s2[start]] -= 1
                if counter_s2[s2[start]] == 0:
                    del counter_s2[s2[start]]
                start += 1
        return False