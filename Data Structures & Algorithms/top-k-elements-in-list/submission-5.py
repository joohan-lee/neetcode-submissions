class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Way 1. Built-in Sort (python timsort) - Time: O(nlogn), Space: O(n)
        # Way 2. heap - Time: O(nlogk), Space: O(k)
        # Way 3. Bucket Sort - Time: O(n), Space: O(n)

        n = len(nums)
        count = {}

        # Count each number
        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1
        # print(f'{count=}')
        # Create an array with idx==count, value=elem
        freq = defaultdict(list)
        for elem, cnt in count.items():
            freq[cnt].append(elem)
        # print(f'{freq=}')
        # Get k-th frequent elem
        j=n
        res = []
        while j >= 0:
            for elem in freq[j]:
                res.append(elem)
                if len(res) == k:
                    return res
            # print(f'{j=}, {res=}, {k=}')
            j -= 1
        return res

        

