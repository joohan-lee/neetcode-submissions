class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Leave the shortest intervals if overlap exists at each index.
        '''
        # Min Heap
        intervals.sort()
        min_heap = []

        res, i = {}, 0

        for q in sorted(queries):
            
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i][0], intervals[i][1]
                heapq.heappush(min_heap, ((r-l+1), r))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            res[q] = min_heap[0][0] if min_heap else -1
        
        return [res[q] for q in queries]