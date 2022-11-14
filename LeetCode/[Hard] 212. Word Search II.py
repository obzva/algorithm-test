import collections
from typing import *


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        word_key = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[word_key] = word

        matches = []

        def backtrack(row: int, col: int, parent: collections.defaultdict):
            char = board[row][col]
            curr_node = parent[char]

            match = curr_node.pop(word_key, False)
            if match:
                matches.append(match)

            board[row][col] = '#'
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= row + dr < m and 0 <= col + dc < n and board[row + dr][col + dc] in curr_node:
                    backtrack(row + dr, col + dc, curr_node)

            board[row][col] = char

            if not curr_node:
                parent.pop(char)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return matches
