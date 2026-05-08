class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        min_k = 1, max_k = max(piles)
        Can achieve min time(h) if koko eats in max_k speed. => h = len(piles)
        Can achieve max time(h) if koko eats in 1 banana per hour. => sum(piles)
        Need to find minimum k to finish all in h hours.
        """

        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r-l) // 2
            if self.canFinish(piles, mid, h):
                # If possible, lower the k
                r = mid - 1
            else:
                # Otherwise, increase k
                l = mid + 1
        
        return l
    
    def canFinish(self, piles, k, h):
        t = 0
        for p in piles:
            t += math.ceil(p / k)
        
        return t <= h