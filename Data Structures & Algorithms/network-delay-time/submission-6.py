class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        벨만포드 알고리즘의 동작과정은 다음과 같습니다.

        1. 모든 정점까지의 거리를 무한대로 초기화 합니다. 단 출발 정점의 초기값을 0으로 합니다.
        2. 정점의 개수 - 1 번 만큼 반복을 진행 합니다.
            2-1. 모든 간선을 순회하며 거리를 갱신합니다.
            2-2. 기존 값보다 더 작은 값으로 업데이트 된다면 거리를 갱신합니다.
        3. 음의 사이클을 확인하기 위해 한 번 더 거리를 갱신하여 업데이트 되는지 확인합니다.
            3-1. 업데이트 된다면 음의 사이클이 존재하는 것입니다.
        4. 최종적으로 구한 경로들이 출발점에서의 최단 경로 입니다.
        '''
        # Bellman Ford
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        for i in range(1, n+1):
            # 모든 간선을 순회.
            for u, v, t in times:
                # u->v로 갈 때 이전 보다 거리가 줄어들면 dist[v] 업데이트.
                if dist[u] + t < dist[v]:
                    dist[v] = dist[u] + t
        res = max(dist.values())
        return res if res < float('inf') else -1