class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        # Store values in heap with index so that we can remove them if they are out of window
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        res = [-max_heap[0][0]]
        # print(f'{max_heap=}')
        for i in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            # print(f'{max_heap=}')
            res.append(-max_heap[0][0])
        
        return res