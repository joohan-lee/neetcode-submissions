class Node:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26 # a - z
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        
        return True
        
        