class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range(len(nums) + 1)] # index=occurrence(frequency), values=numbers occurred the same number of times as index (occurred exactly index times)

        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        for num, f in count_map.items():
            freq[f].append(num)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i]:
                res.extend(freq[i])
            if len(res) == k:
                break
        
        return res
            

