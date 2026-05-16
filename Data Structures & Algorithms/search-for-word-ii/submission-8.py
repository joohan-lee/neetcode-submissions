class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children: Optional[TrieNode] = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        if not word:
            raise ValueError
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True
    
    def search(self, word):
        if not word:
            return False
        
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for w in words:
            trie.addWord(w)
        
        res = set()
        def dfs(node, r, c, word):
            if not (0 <= r < ROWS
                and 0<= c < COLS
                and board[r][c] != '#'
                and node.children[ord(board[r][c]) - ord('a')]):
                return
            
            
            # 노드를 현재 char로 옮ㄱ기기.
            cur_idx = ord(board[r][c]) - ord('a')
            node = node.children[cur_idx]
            # word에 현재 char넣기.
            word.append(board[r][c])
            tmp = board[r][c]
            board[r][c] = '#' # mark as visited

            if node.is_end:
                res.add("".join(word))
            
            dfs(node, r+1, c, word)
            dfs(node, r-1, c, word)
            dfs(node, r, c+1, word)
            dfs(node, r, c-1, word)
            
            word.pop() # 다시 빼고 위로 올라가 다른 방향 가보기
            board[r][c] = tmp # revert

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                dfs(trie.root, r,c, [])
        return list(res)