class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # way1. Brute Force - time: O(n^3), space: O(1)
        # way2. Hash map using two sum. - time: O(n^2), space: O(n)

        '''
        [-1, 0,1,2,-1,-4]
        [-1,0,1], [-1,2,-1]
        [0,1,-1]

        [-4,-1,-1,0,1,2]
        [-1,-1,2], [-1,0,1]
        '''

        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i and nums[i-1] == nums[i]:
                continue
            st = self.twoSum(nums[i+1:], -n)
            # print(f'{st=}')
            for t in st:
                res.append([n, t[0], t[1]])
        return res
        
    def twoSum(self, nums: List[int], target: int) -> Set[Tuple[int]]:
        # [n1, n2] summing up to target
        # Use hash map or two pointers (b/c sorted)
        '''
        [0,1,1,1,12,2]
        target:2
        '''
        mp = defaultdict(int) # {num: idx}
        res = set()
        for i in range(len(nums)):
            n = nums[i]
            comp = target - n
            if comp in mp:
                res.add((comp, n))
            mp[n] = i
        return res