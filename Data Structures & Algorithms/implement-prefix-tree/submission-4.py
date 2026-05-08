class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')    
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            
            node = node.children[idx]
        
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] == None:
                return False
            node = node.children[idx]
        
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] == None:
                return False
            node = node.children[idx]
            
        return True
        