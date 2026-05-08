class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
            d       e       f
         g  h i   
        '''
        char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []
        def dfs(i, curr):
            if i == len(digits):
                res.append(''.join(curr))
                return
            
            curr_digit_chars = char_map[digits[i]]
            for j in range(len(curr_digit_chars)):
                curr.append(curr_digit_chars[j])
                dfs(i+1, curr)
                curr.pop()

        n = len(digits)
        res = []
        dfs(0, [])
        return res
        
        