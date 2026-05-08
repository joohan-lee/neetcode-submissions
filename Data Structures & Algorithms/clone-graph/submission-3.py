"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        1. 시작 노드 복제 + 큐에 넣기
        2. 큐에서 하나 꺼냄 (cur)
        3. cur의 이웃들 순회:
            - 처음 보는 이웃? → 복제 + 큐에 추가
            - 복제된 cur ↔ 복제된 nei 연결
        4. 큐 빌 때까지 반복
        """
        # 엣지 케이스: 빈 그래프
        if not node:
            return None
        
        # oldToNew: 원본 노드 → 복제 노드 매핑
        # 역할 1) 방문 여부 체크 (키 존재 = 방문함)
        # 역할 2) 원본-복제 연결고리 저장
        oldToNew = {}
        
        # 시작 노드 처리 (루프 전에 수동으로)
        oldToNew[node] = Node(node.val)
        q = deque([node])
        
        while q:
            cur = q.popleft()  # 현재 처리할 원본 노드
            
            for nei in cur.neighbors:
                # [노드 생성] 처음 보는 이웃이면 복제본 생성 + 큐에 추가
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)  # 방문처리 = 복제본 생성
                    q.append(nei)                   # 나중에 이 노드의 이웃도 탐색
                
                # [간선 연결] 복제본끼리 이웃 관계 설정
                # if 밖에 있음 → 이미 생성된 노드여도 간선은 연결해야 하니까
                oldToNew[cur].neighbors.append(oldToNew[nei])
        
        # 시작 노드의 복제본 반환
        return oldToNew[node]