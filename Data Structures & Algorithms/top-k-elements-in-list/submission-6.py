class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Way 1. Built-in Sort (python timsort) - Time: O(nlogn), Space: O(n)
        # Way 2. heap - Time: O(nlogk), Space: O(k)
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        min_heap = []
        for key, v in counter.items():
            heapq.heappush(min_heap, (v, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [x for _,x in min_heap]

        # Way 3. Bucket Sort - Time: O(n), Space: O(n)
        """
        빈도 수 범위가 작으니 인덱스로 쓸 수 있다. -> Bucket Sort 가능.
        빈도 수를 인덱스로 하는 버킷을 만들고 각 버킷에 해당 빈도수의 숫자를 기록.
        총 n+1개의 버킷을 만들기: [[] for _ in range(n+1)]
        """

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

        

