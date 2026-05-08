class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {} # Hash Map {'character': TrieNode}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            # dfs=> if word[j:] is included in Trie starting from given root node
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Recursive call.
                    # If any child satisfies condition, true. 
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.endOfWord
        
        return dfs(0, self.root)


