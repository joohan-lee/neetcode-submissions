class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # {tuple: list[str]}

        for s in strs:
            ch_cnt = [0] * 26
            for ch in s:
                ch_cnt[ord(ch) - ord('a')] += 1
            groups[tuple(ch_cnt)].append(s)
        
        return list(groups.values())