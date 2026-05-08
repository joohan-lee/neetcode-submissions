class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Way 1. Reverse string
        # newStr = ''
        # for ch in s:
        #     if ch.isalnum():
        #         newStr += ch.lower()
        # return newStr == newStr[::-1]

        # Way 2. Two pointers

        l, r = 0, len(s)-1

        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
            elif not self.isAlphaNum(s[r]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def isAlphaNum(self, ch):
        return (ord('a') <= ord(ch) <= ord('z') or
                ord('A') <= ord(ch) <= ord('Z') or
                ord('0') <= ord(ch) <= ord('9'))