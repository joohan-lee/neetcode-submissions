class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        222
        111
        ====
        222
       2220
      22200
    ========
      24642

        356
        247
        ===
       2492
      1424
      712
      =====
      87932
        """
        if num1 == "0" or num2 == "0":
            return "0"
            
        res = [0] * (len(num1) + len(num2)) # 최대 길이: n+m 

        for i1 in range(len(num1) - 1, -1, -1):
            for i2 in range(len(num2) - 1, -1, -1):
                n1 = ord(num1[i1]) - ord('0')
                n2 = ord(num2[i2]) - ord('0')
                digit = n1 * n2

                p1 = i1 + i2 + 1 # 현재 자리.
                p2 = i1 + i2 # 현재 자리에서 캐리가 발생하면 줄 다음 자리.
                
                res[p1] += digit
                res[p2] += (res[p1] // 10)
                res[p1] = res[p1] % 10
        
        # Remove leading zeros
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg+=1
        return "".join(map(str, res[beg:]))