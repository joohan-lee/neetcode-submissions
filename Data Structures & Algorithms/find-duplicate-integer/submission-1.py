class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        모든 element는 [1, n] 값을 가지므로 index 0에서 출발하여 nums[0] -> nums[nums[0]] -> nums[nums[nums[0]]]
        이런식으로 linked list를 그릴 수 있다.
        """
        slow, fast = 0, 0
        n = len(nums)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow