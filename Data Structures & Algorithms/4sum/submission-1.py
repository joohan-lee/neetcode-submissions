class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def twoSum(arr, t):
            hash_map = {}
            ret = set()
            for i in range(len(arr)):
                c = t - arr[i]
                if c in hash_map:
                    ret.add((arr[i], c))
                hash_map[arr[i]] = i
            # print(f'{ret=}')
            return ret


        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                subset = twoSum(nums[j+1:], target - (nums[i] + nums[j]))
                for a,b in subset:
                    res.append([nums[i],nums[j],a,b])
                
        return res