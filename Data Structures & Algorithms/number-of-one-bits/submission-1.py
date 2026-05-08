class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n = n & (n-1) # Remove lowest set bit (1 bit)
            cnt += 1
        return cnt
        # Time: O(k), where k is the number of 1s in bits
        