class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        0 1 2 3 4 5
          ---
            -----
          -------
              -----
        '''
        intervals.sort(key=lambda x: x[0])

        interval = intervals[0]
        remove_cnt = 0
        for i in range(1, len(intervals)):
            if interval[1] > intervals[i][0]:
                # If overlaps, remove longer one.
                remove_cnt += 1
                interval[1] = min(interval[1], intervals[i][1])
            else:
                interval = intervals[i]
            # print(f'{i=}, {interval=}, {intervals[i]=}, {remove_cnt=}')
        
        return remove_cnt
