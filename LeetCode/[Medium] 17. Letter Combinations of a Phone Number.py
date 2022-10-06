import collections
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # RECURSIVE
        #
        # if not digits:
        #     return []
        #
        # dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # result = []
        #
        # def dfs(index, path):
        #     if len(path) == len(digits):
        #         result.append(path)
        #         return
        #
        #     for j in dic[digits[index]]:
        #         dfs(index + 1, path + j)
        #
        # dfs(0, '')
        # return result

        # ITERATIVE

        if not digits:
            return []

        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        queue = collections.deque([])

        for digit in digits:
            new_letters = dic[digit]
            curr_len = len(queue)
            if not curr_len:
                queue.extend(new_letters)
            else:
                for _ in range(curr_len):
                    prev_letter = queue.popleft()
                    queue.extend([prev_letter + new_letter for new_letter in new_letters])

        return queue
