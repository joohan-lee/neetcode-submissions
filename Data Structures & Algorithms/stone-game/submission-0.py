class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        Alice takes
                0
            /         \
        start         end
       /   \           /  \ 
      s    e          s    e
        """
        total = sum(piles)
        l, r = 0, len(piles) - 1

        alice = 0
        while l < r:
            alice += max(piles[l], piles[r])
            l += 1
            r -= 1
        
        return alice > total / 2