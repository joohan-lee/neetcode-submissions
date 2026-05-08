class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)
        for ch1, ch2 in zip(s, t):
            hmap1[ch1] += 1
            hmap2[ch2] += 1
        return hmap1 == hmap2