class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i
        
        res = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(last_idx[c], end) # 현재까지 나온 캐릭터들의 끝 위치.

            if i == end:
                # 현재 그룹 마지막 도착하면 추가하고 사이즈 초기화
                res.append(end - start + 1)
                start = i + 1
        return res

            