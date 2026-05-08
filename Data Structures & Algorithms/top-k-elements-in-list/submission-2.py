class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        min_heap = []
        for key, val in count_map.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [x for _, x in min_heap]
