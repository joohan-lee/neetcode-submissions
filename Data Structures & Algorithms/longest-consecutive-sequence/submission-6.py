class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Way 1. Sort. => Time: O(nlogn), Space: O(n)
        # Way 2. Hash Set => Time: O(n), Space: O(n)
        # Way 3. Hash Map => Time: O(n), Space: O(n)

        st = set(nums)
        res = 0
        for n in st:
            if n-1 not in st:
                a = n
                while a in st:
                    a += 1
                res = max(res, a - n)
        return res
