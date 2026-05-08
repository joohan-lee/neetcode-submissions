class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            i = (l + r) // 2 # A에서 i까지의 elem이 A의 left part. i+1 부터 right part.
            j = half - i - 2 # B에서 j까지의 elem이 B의 left part. j+1 부터 right part.
            # 즉, i까지의 elem 수는 (i+1)개 이고, j 까지의 elem 수는 (j+1) 개 이고,
            # (i+1) + (j+1) = (i+1) + (half - i - 2 + 1) = half 개가 된다.

            Aleft = A[i] if i >=0 else -float("inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf") 
            # 만약, A = [1,2,3,4,5] / B = [9,10,11,12,13,14,15] 처럼 A의 배열이 A left part로 다 쓰여야 하는 경우,
            # Aright 는 그냥 무한대로 해주어서 Bleft 와 밑에서 비교한다.

            Bleft = B[j] if j >= 0 else -float("inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # Aleft 값이 Bright 보다 크면, A 값을 덜 사용해야함.
                r = i - 1
            elif Bleft > Aright:
                # Bleft 값이 Aright보다 크면, A 값을 더 사용해야함.
                l = i + 1