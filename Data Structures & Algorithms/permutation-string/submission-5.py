class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for ch in s1:
            s1Count[ord(ch) - ord('a')] += 1
        
        start = 0
        for end in range(len(s2)):
            s2Count[ord(s2[end]) - ord('a')] += 1
            # print(f'{s1Count=}')
            # print(f'{s2Count=}')
            if s1Count == s2Count:
                return True
            
            if end - start + 1 >= len(s1):
                s2Count[ord(s2[start]) - ord('a')] -= 1
                start += 1

        return False
