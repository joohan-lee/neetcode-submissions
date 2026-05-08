class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        11 XOR 11 = 00
        Same numbers will be zero at the end.

        a XOR b XOR c XOR a XOR b = (a XOR a) XOR (b XOR b) XOR c
        = 0 XOR 0 XOR c
        = 0 XOR c
        = c
        """
        res = 0
        for n in nums:
            res ^= n
        return res