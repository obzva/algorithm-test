class TrieNode:
    def __init__(self):
        self.search = False
        self.next = dict()


class Trie:

    def __init__(self):
        self.HEAD = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.HEAD
        for char in word:
            if char in pointer.next:
                pointer = pointer.next[char]
            else:
                node = TrieNode()
                pointer.next[char] = node
                pointer = node
        pointer.search = True

    def search(self, word: str) -> bool:
        pointer = self.HEAD
        for char in word:
            if char not in pointer.next:
                return False
            else:
                pointer = pointer.next[char]
        return pointer.search

    def startsWith(self, prefix: str) -> bool:
        pointer = self.HEAD
        for char in prefix:
            if char not in pointer.next:
                return False
            else:
                pointer = pointer.next[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
