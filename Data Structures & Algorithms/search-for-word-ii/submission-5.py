class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        
        node.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = set()

        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        def dfs(node, r, c, w):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r,c) in visited:
                return
            
            ch = board[r][c]
            idx = ord(ch) - ord('a')
            # Trie에 없는 단어면 바로 return
            if not node.children[idx]:
                return

            
            visited.add((r,c))
            w.append(ch)
            node = node.children[idx]
            if node.end_of_word:
                res.add("".join(w))
            
            
            dfs(node, r + 1, c, w)
            dfs(node, r - 1, c, w)
            dfs(node, r, c + 1, w)
            dfs(node, r, c - 1, w)
            
            w.pop()
            visited.remove((r,c))

        
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                dfs(trie.root, r, c, [])
        return list(res)

