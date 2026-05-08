"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Add intervals to min_heap and pop it if new interval starts after ending last one

        intervals.sort(key=lambda x: x.start)
        
        min_heap = [] # (end, start)

        for i in range(len(intervals)):
            if not min_heap or min_heap[0][0] > intervals[i].start:
                heapq.heappush(min_heap, (intervals[i].end, intervals[i].start))
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (intervals[i].end, intervals[i].start))
        return len(min_heap)
