class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)

        for ch in s1:
            count[ch] += 1

        for i in range(len(s2)):
            count2 = defaultdict(int)
            for ch2 in s2[i: i + len(s1)]:
                count2[ch2] += 1
            if count == count2:
                return True
        return False