class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1 and n not in seen:
            n_str = str(n)
            seen.add(n)
            total = 0
            for c in n_str:
                total += int(c) ** 2
            n = total
        return True if n == 1 else False
