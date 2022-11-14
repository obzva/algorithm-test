from typing import *


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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        subs = []

        def get_sub(sub: str, path: List[str]):
            if not sub:
                subs.append(' '.join(path))
            for i in range(len(sub)):
                if trie.search(sub[:i + 1]):
                    get_sub(sub[i + 1:], path + [sub[:i + 1]])

        get_sub(s, [])
