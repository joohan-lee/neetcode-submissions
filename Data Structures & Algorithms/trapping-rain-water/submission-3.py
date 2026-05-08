class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers
        # Time: O(n), Space: O(1)
        """
        물이 고이는 원리: 특정 위치에서 물이 고이는 양 = min(왼쪽 최대 높이, 오른쪽 최대 높이) - 현재 높이
        이게 가장 중요한 출발점이야. 물은 양쪽 벽 중 더 낮은 쪽까지만 차오를 수 있으니까.
        💡 투 포인터 접근의 직관
        여기서 핵심 질문: "왼쪽 최대/오른쪽 최대를 굳이 전부 미리 계산할 필요가 있을까?"
        관찰:

        leftMax < rightMax 라면 → 왼쪽 포인터 위치의 물 높이는 무조건 leftMax에 의해 결정됨
        왜? 오른쪽에 더 높은 벽이 있다는 게 확실하니까, 오른쪽의 정확한 값은 안 중요함.

        반대로 leftMax > rightMax 라면 -> 더 낮은 오른쪽 벽에 의해 물 높이 결정됨.
        """
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        area = 0
        # 마지막 위치까지 계산하려면 equal 필요
        while l <= r:
            if left_max < right_max:
                area += max((left_max - height[l]), 0)
                left_max= max(left_max, height[l])
                l += 1
            else:
                area += max((right_max - height[r]), 0)
                right_max= max(right_max, height[r])
                r -= 1
        
        return area

