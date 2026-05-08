class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countSetBit(i))
        return res
    
    def countSetBit(self, n: int) -> int:
        cnt = 0
        while n:
            n = n & (n-1)
            cnt += 1
        return cnt