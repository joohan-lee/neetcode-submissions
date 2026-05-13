class MedianFinder:

    def __init__(self):
        self.small = [] # half smaller data. max_heap
        self.large = [] # half larger data. min_heap

    def addNum(self, num: int) -> None:
        # Add to small (max_heap) by default
        heapq.heappush(self.small, -num)

        # to satisfy small_top <= large_top, move added value to large.
        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Keep |len(small) - len(large)| <= 1
        if len(self.small) > len(self.large) + 1:
            # Move top from small to large
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            # Move top from large to small
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if not self.small and not self.large:
            # 문제 조건에 이 함수가 호출될 때 최소 하나 요소는 있을거라고 조건있긴함.
            raise ValueError
        
        if (len(self.small) + len(self.large)) % 2 == 0:
            # even
            return (-self.small[0] + self.large[0]) / 2
        else:
            # odd
            return -self.small[0] if len(self.small) > len(self.large) else self.large[0]
        