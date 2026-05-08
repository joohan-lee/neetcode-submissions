class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Leave the shortest intervals if overlap exists at each index.
        '''
        # Brute Force
        def find_minimum(n):
            min_len = float('inf')
            for i in range(len(intervals)):
                interval = intervals[i]
                if interval[0] <= n <= interval[1]:
                    curr_len = interval[1]-interval[0] + 1
                    min_len = min(curr_len, min_len)
            return min_len if min_len != float('inf') else -1

        res = []
        for q in queries:
            res.append(find_minimum(q))
        return res