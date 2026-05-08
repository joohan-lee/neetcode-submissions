class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        for start in range(len(s2) - len(s1)+1):
            if self._isSame(s2[start:start+len(s1)],freq):
                return True
        return False
    
    def _isSame(self, s, freq):
        s_freq = {}
        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1
        
        # print(f'{s_freq=}, {freq=}')
        return s_freq == freq
                