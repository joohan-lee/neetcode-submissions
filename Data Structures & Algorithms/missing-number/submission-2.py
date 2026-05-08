class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        00 -> 0

        01 -> 1
        10 -> 2
        11

        00
        10
        [3, 0, 2]
        = 3^
        
        idx0 ^ val0 ^ idx1 ^ val1 ... 
        
        """
        n = len(nums)
        xorr = n

        for i in range(n):
            xorr ^= i # 완전 집합의 0~n-1 (위에서 n도 넣었으니 사실상 0~n)
            xorr ^= nums[i] # 불완전 집합 (하나 부족)

        # (0~n) ^ (0~n-1) 하면 우측에 하나 짝이 없는 한가지가 남을 것.
        return xorr