class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            # tuple as key
            cnt = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                cnt[idx] += 1
            anagrams[tuple(cnt)].append(s)
        
        return list(anagrams.values())
            