from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word = False
        # self.children = {}
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            # if char not in node.children:
            #     node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))     # True
    print(trie.search("app"))       # False
    print(trie.startsWith("app"))   # True
    trie.insert("app")
    print(trie.search("app"))       # True