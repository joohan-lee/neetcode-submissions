class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        sorted_map = sorted(count_map.items(), key = lambda x: x[1], reverse=True)
        res = []
        # print(f'{sorted_map=}')
        for key, val in sorted_map:
            res.append(key)
            if len(res) == k:
                break
        return res