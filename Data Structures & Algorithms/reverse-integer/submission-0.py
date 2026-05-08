class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        sign = 1 if x >= 0 else -1
        str_x = str(abs(x))
        str_x = str_x[::-1]
        return sign * int(str_x) if int(str_x) <= 0x7FFFFFFF else 0