class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic deque
        """
        deq = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            # pop smaller values from q top
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            # remove values out of window
            if l > deq[0]:
                deq.popleft()
            
            # Add output from leftmost index at deque. (Since Monotonic deque, leftmost is biggest)
            if (r+1) >=k:
                res.append(nums[deq[0]]) 
                l += 1 # Move window
            
        return res



