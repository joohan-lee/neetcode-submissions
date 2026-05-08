class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1012
["1","2",...,"26"]

        1. If first one or two characters equal to one of keys ["1", "2",..."26"],
            traverse deeper with the rest of characters.
            If no key matched, return 0
        2. If we visited all chars in s, add +1 to the number of ways.

        """

        def dfs(i, remaining):
            # print(f'{i=}', f'{remaining=}')
            if i == len(s):
                return 1
            
            ways_at_curr_node = 0
            for j in range(1, 27):
                s_j = str(j)
                if s_j == remaining[:len(s_j)]:
                    ways_at_curr_node += dfs(i+len(s_j), remaining[len(s_j):])
            
            return ways_at_curr_node
        
        return dfs(0, s)
                
        