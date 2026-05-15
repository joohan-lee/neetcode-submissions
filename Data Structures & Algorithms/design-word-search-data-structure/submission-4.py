class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        print(f'{word=}')
        def dfs(node, cur):
            for i in range(cur, len(word)):
                ch = word[i]
                idx = ord(ch) - ord('a')
                if ch == ".":
                    for j in range(len(node.children)):
                        if node.children[j] and dfs(node.children[j], i+1):
                            return True
                    return False # "."으로 못찾았으면 없는 거임. 안해주면 밑에서 if문과 다음 node 이동 시 out of index.
                # print(f'{idx=}, {ch=}')
                if node.children[idx] is None:
                    return False
                node = node.children[idx]
                
            return node.is_end
        
        return dfs(self.root, 0)