class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(n):
            prev_rate = ratings[i-1] if i-1 >= 0 else float('inf')
            nxt_rate = ratings[i+1] if i+1 < n else float('inf')
            # print(f'{prev_rate=}, {nxt_rate=}')
            if (ratings[i] > prev_rate):
                prev_candy = candies[i-1] if i - 1 >= 0 else 1
                candies[i] = max(candies[i], prev_candy + 1)
            if (ratings[i] > nxt_rate):
                nxt_candy = candies[i+1] if i + 1 < n else 1
                candies[i] = max(candies[i], nxt_candy + 1)
            # print(f'{i=}, {candies=}')

        for i in range(n-1, -1, -1):
            prev_rate = ratings[i-1] if i-1 >= 0 else float('inf')
            nxt_rate = ratings[i+1] if i+1 < n else float('inf')
            # print(f'{prev_rate=}, {nxt_rate=}')
            if (ratings[i] > prev_rate):
                prev_candy = candies[i-1] if i - 1 >= 0 else 1
                candies[i] = max(candies[i], prev_candy + 1)
            if (ratings[i] > nxt_rate):
                nxt_candy = candies[i+1] if i + 1 < n else 1
                candies[i] = max(candies[i], nxt_candy + 1)
            # print(f'{i=}, {candies=}')
        
        return sum(candies)
