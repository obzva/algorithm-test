import collections
from typing import *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # n = len(beginWord)
        # word_queue = collections.deque()
        # word_queue.append(beginWord)
        # visited = set()
        # level = 0
        # while word_queue:
        #     level += 1
        #     iter_no = len(word_queue)
        #     for _ in range(iter_no):
        #         the_word = word_queue.popleft()
        #         if the_word == endWord:
        #             return level
        #         visited.add(the_word)
        #         for i in range(n):
        #             for word in wordList:
        #                 if word not in visited and all(word[j] == the_word[j] for j in range(n) if j != i):
        #                     word_queue.append(word)
        #                     visited.add(word)
        # return 0

        # USING HASHMAP

        n = len(beginWord)

        hashmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                hashmap[word].append(word[:i] + '_' + word[i + 1:])

        word_queue = collections.deque()
        word_queue.append(beginWord)
        level = 0
        while word_queue:
            level += 1
            iter_no = len(word_queue)
            for _ in range(iter_no):
                the_word = word_queue.popleft()
                if the_word == endWord:
                    return level
                for i in range(n):
                    tmp = set()
                    target = the_word[:i] + '_' + the_word[i + 1:]
                    for word in hashmap:
                        if hashmap[word][i] == target:
                            tmp.add(word)
                    for word in tmp:
                        del hashmap[word]
                    word_queue.extend(list(tmp))
        return 0


