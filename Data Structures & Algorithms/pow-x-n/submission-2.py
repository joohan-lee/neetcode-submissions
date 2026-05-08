class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        binary exponentiation
        x^n = (x^2)^(n/2) if n is even
            = x * (x^2)^((n-1)/2) if n is odd

        For example,
            2^20 = (2^2)^10
            4^10 = (4^2)^5
            16^5 = 16 * (16^2)^2
            16 * (256)^
        """
        if n==0: return 1
        if n < 0:
            # return 1 / x * self.myPow(x, n+1) # 이렇게하면 n만큼 재귀됨.
            return 1 / self.myPow(x, -n) # 양수로 바꿔줘야 밑에 규칙을 사용하여 logn으로 가능.

        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, (n-1)/2)
