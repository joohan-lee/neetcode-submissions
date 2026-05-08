class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        st = set()
        cnt = 1
        for n in nums:
            if n in st:
                return n
            st.add(n)
        return
            