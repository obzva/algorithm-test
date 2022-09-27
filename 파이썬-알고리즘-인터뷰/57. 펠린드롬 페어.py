"""
Burte-force
"""

from typing import *


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                new_word = words[i] + words[j]
                if new_word == new_word[::-1]:
                    answer.append([i, j])
        return answer
