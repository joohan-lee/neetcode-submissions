class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS = 최단 거리 when weight = 1
        if amount == 0:
            return 0
        
        seen = set()
        q = deque([0]) # 0 amount 시작
        level = 0

        while q:

            len_q = len(q)

            for i in range(len_q):
                cur_amt = q.popleft()

                if cur_amt == amount:
                    # Since it is dfs, first found one is in the minimum distance.
                    return level

                # Traverse adjacent
                for c in coins:
                    nc = cur_amt + c
                    if nc not in seen and nc <= amount:
                        q.append(nc)
                        seen.add(nc)
            level += 1
            

        return -1 