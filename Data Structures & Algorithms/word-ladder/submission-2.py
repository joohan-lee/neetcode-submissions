class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ''' BFS with generic word'''
        if endWord not in wordList or not endWord:
            return 0

        combination_maps = defaultdict(set)
        L = len(beginWord)
        for word in wordList+[beginWord]:
            for i in range(L):
                g_word = word[:i] + "*" + word[i+1:]
                combination_maps[g_word].add(word)
        
        q = deque([(beginWord, 1)]) # current_word, level
        visited = set()
        while q:
            curr_word, level = q.popleft()
            for i in range(L):
                curr_generic_word = curr_word[:i] + "*" + curr_word[i+1:]

                for nei in combination_maps[curr_generic_word]:
                    if nei == endWord:
                        return level + 1
                    
                    if nei not in visited:
                        q.append(((nei, level + 1)))
                        visited.add(nei)

        return 0
        