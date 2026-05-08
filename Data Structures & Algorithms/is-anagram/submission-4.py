class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map1, hash_map2 = defaultdict(int), defaultdict(int)
        for ch1, ch2 in zip(s,t):
            hash_map1[ch1] = hash_map1.get(ch1,0) + 1
            hash_map2[ch2] = hash_map2.get(ch2,0) + 1
        
        return hash_map1 == hash_map2