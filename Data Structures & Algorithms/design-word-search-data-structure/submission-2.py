class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        
        node.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, i):
            if not node:
                return False
            if i == len(word):
                return node.end_of_word
            
            for j in range(i, len(word)):
                ch = word[j]
                if ch == ".":
                    for child in node.children:
                        if dfs(child, j+1):
                            return True
                    return False # "."으로 못찾았으면 없는 거임.
                idx = ord(ch) - ord('a')
                if node.children[idx] == None:
                    return False
                
                node = node.children[idx]
            
            return node.end_of_word
        
        return dfs(curr, 0)