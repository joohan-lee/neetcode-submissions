class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Way 1. Sort. => Time: O(nlogn), Space: O(n)
        # Way 2. Hash => Time: O(n), Space: O(n)

        st = set(nums)
        
        max_len = 0
        for n in st:
            curr_len = 0
            if n - 1 not in st:
                # Can be a starting point
                while n in st:
                    curr_len += 1
                    n += 1
                max_len = max(max_len, curr_len)
        
        return max_len