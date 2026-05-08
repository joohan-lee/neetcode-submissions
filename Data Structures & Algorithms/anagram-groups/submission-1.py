class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        for s in strs:
            # t = getTuple(s)
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            t = tuple(cnt)
            if t not in h_map:
                h_map[t] = [s]
            else:
                h_map[t].append(s)
        
        return list(h_map.values())