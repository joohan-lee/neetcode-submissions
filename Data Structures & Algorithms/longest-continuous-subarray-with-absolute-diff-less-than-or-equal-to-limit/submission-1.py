class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []

        res=0

        start = 0
        for end in range(len(nums)):
            heapq.heappush(min_heap, (nums[end], end))
            heapq.heappush(max_heap, (-nums[end], end))

            while abs(-max_heap[0][0] - min_heap[0][0]) > limit:
                start += 1
                # 오래된 값 제거
                while max_heap[0][1] < start:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < start:
                    heapq.heappop(min_heap)
            
            res = max(res, end - start + 1)
        
        return res