"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x: x.start)

        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        num_of_days = 1
        for i in range(1, len(intervals)):
            earliest_end = min_heap[0]
            if earliest_end > intervals[i].start:
                num_of_days += 1
            else:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, intervals[i].end)
        
        return num_of_days


