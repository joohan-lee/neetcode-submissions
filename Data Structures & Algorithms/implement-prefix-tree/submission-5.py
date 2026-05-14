class Node:
    def __init__(self):
        self.is_end = False
        self.children: List[Node] = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                # if none, create a new node.
                node.children[idx] = Node()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                # if none, doesnt exist. ealry return
                return False
            node = node.children[idx]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                # if none, doesnt exist. ealry return
                return False
            node = node.children[idx]
        return True
        