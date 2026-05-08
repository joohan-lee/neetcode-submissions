class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i
        
        res = []
        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1 # 현재까지 size
            end = max(last_idx[c], end) # 현재까지 나온 캐릭터들의 끝 위치.

            if i == end:
                # 현재 그룹 마지막 도착하면 추가하고 사이즈 초기화
                res.append(size)
                size = 0
        return res

            