class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for ch1, ch2 in zip(s, t):
            s_map[ch1] += 1
            t_map[ch2] += 1
        
        return s_map == t_map
