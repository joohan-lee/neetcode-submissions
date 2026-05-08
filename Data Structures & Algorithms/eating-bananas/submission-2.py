class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k가 가능한 값은 1부터 max(piles). (정렬.)
        그 중 최소가 되는 k를 찾는 것.
        """
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r-l) // 2

            if self.canEat(mid, piles, h):
                r = mid - 1
            else:
                l = mid + 1
        return l
    def canEat(self, k, piles, h):
        total_h = 0
        for p in piles:
            t = math.ceil(p / k)
            total_h += t
        
        return total_h <= h