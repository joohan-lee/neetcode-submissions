class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        각 배열이 정렬되어 있으니 단조성 (monotonicity)이 보장됨.
        -> 한 방향이 실패하면 그 방향 전체가 실패 (e.g., 현재 i가 안되면, i보다 큰 값들은 전부 안됨)
        -> Binary search가능.
        [1,5,9]
        [2,4,8]

        짧은 배열을 A로 두고 B에서 필요한 수(j+1)만큼 가져와서 half를 채우는 방식.
        그런데, A가 더 길면 j가 음수가 될 수 있고 음수개만큼 B에서 가져온다는게 말이 안되므로 A를 더 짧게 두고 사용.
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2            # A에서 왼쪽 파티션에 넣을 마지막 인덱스. (즉, i+1개)
            j = half - i - 1 - 1        # B에서 왼쪽 파티션에 넣을 마지막 인덱스. (즉, j+1개)
            # (i+1) + (j+1) = half => j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf') #Aleft는 왼쪽 파티션 마지막 elem, Aright는 우측 파티션 첫 elem
            Aright= A[i+1] if i + 1 < len(A) else float('inf')
            Bleft = B[j]   if j >=0 else float('-inf')
            Bright = B[j+1]if j+1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # odd
                    return min(Aright, Bright)
                else: # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1 # 이미 i번째도 포함될 수 없다면, i번째보다 더 큰건 모두 버려도 됨.
            elif Bleft > Aright:
                l = i + 1 # i번째 포함했는데도 B에서 더 빼야한다면, i번째 다음 절반까지 포함하도록 확인해야함.
            
            
