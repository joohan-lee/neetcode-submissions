class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for ch in s:
            if ch.isalnum():
                newStr += ch
        s = newStr.lower()
        # print(f'{s=}')
        return s[:] == s[::-1]