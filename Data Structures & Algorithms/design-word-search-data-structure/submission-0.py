class TrieNode:
    def __init__(self):
        self.child = {}
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.isLeaf = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for kid in cur.child.values():
                        if dfs(i+1, kid):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.isLeaf
        
        return dfs(0, self.root)
