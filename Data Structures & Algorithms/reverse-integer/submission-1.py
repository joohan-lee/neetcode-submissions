class Solution:
    def reverse(self, x: int) -> int:
        # max_int = 0x7FFFFFFF
        # min_int = 0xFFFFFFFF
        min_int = -2**31
        max_int = 2**31 - 1


        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            
            # res를 증가시키기 전에 overflow가능성 확인.
            if res > max_int // 10 or (res == max_int//10 and digit > max_int % 10):
                return 0
            # res를 증가시키기 전에 underflow가능성 확인.
            if res < min_int // 10 or (res == min_int // 10 and digit < min_int % 10):
                return 0

            res = (res * 10) + digit
        return res