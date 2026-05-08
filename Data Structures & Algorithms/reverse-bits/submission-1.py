class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            ith_bit = (n >> i) & 1 # i-th bit
            reversed_n = reversed_n | (ith_bit << (31-i)) # place it in the other side
        return reversed_n