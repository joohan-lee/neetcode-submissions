class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 어차피 1만 더하는거니까 간단하게 구현.

        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0 # 현재 digit이 9이면 1 더했을 때 0이되고, carry가 1 더해지므로 그 다음 자릿수에 +1 후 리턴.
        
        return [1] + digits # 여기까지 온다면 모든 자릿수가 9였고, the most significant digit에 1 추가.