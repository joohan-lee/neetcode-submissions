class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!= 1 and n not in seen:
            seen.add(n)
            n = self.getSumOfSquares(n)
        
        return True if n == 1 else False

    def getSumOfSquares(self, n):
        total = 0
        while n:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total
            
