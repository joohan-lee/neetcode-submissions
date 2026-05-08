class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            reversed_n = reversed_n | (n & 1)
            if i < 31: # 마지막이 아닐 때만 shift
                reversed_n <<= 1
            n >>= 1
            # print(f'{bin(n)=}')
            # print(f'{bin(reversed_n)=}')
        return reversed_n