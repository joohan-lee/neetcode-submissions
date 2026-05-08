class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            new_digit = digits[i] + carry
            if i == len(digits) - 1:
                new_digit += 1
            carry = new_digit // 10
            new_digit = new_digit % 10
            res.append(new_digit)
        
        if carry:
            res.append(carry)
        res.reverse()
        return res