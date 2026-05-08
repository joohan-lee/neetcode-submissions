class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        
        '''
        def _can_go_next(curr_s, next_s):
            diff = 0
            for ch1, ch2 in zip(curr_s, next_s):
                if ch1 != ch2:
                    diff += 1
            return diff == 1
        
        def dfs(word, level):
            nonlocal min_level
            if word == endWord:
                min_level = min(min_level, level)
                return
            
            visited.add(word)
            for next_word in wordList:
                if next_word not in visited and _can_go_next(word, next_word):
                    dfs(next_word, level+1)
            visited.remove(word)
        
        min_level = float('inf')
        visited = set()
        dfs(beginWord, 1)
        return min_level if min_level != float('inf') else 0
