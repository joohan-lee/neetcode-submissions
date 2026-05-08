class MedianFinder:

    def __init__(self):
        self.small = [] # half smaller data. max_heap
        self.large = [] # half larger data. min_heap

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] > num:
            # Add to small group
            heapq.heappush(self.small, -num)
        else:
            # Add to large group
            heapq.heappush(self.large, num)
        
        # 둘의 크기 차이가 2개 이상이면 하나를 반대편으로 이동.
        if len(self.small) > len(self.large) + 1:
            # 작은 절반에서 제일 큰걸 큰 절반으로 이동.
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            # 큰 절반(min heap)에서 제일 작은 걸 작은 절반으로 이동.
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        print(f'{self.large=}, {self.small=}')
        len_large = len(self.large)
        len_small = len(self.small)
        if (len_large + len_small) % 2:
            # odd
            if len_large > len_small:
                return self.large[0]
            else:
                return -self.small[0]
        else:
            # even
            return (self.large[0] - self.small[0]) / 2

        
        