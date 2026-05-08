class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = []
        for tri in triplets:
            if tri[0] <= target[0] and tri[1] <= target[1] and tri[2] <= target[2]:
                candidates.append(tri)
        
        a_max, b_max, c_max = 0, 0, 0
        for c in candidates:
            a_max = max(a_max, c[0])
            b_max = max(b_max, c[1])
            c_max = max(c_max, c[2])
        return [a_max, b_max, c_max] == target