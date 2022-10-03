from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # SOLUTION NO 1
        #
        # answer = ""
        # strs_map = list(map(collections.deque, strs))
        # for i in range(len(strs[0])):
        #     prefix = strs_map[0].popleft()
        #     for j in range(1, len(strs_map)):
        #         if not strs_map[j] or strs_map[j].popleft() != prefix:
        #             return answer
        #     answer += prefix
        # return answer

        # SOLUTION NO 2
        #
        # for i in range(len(strs[0])):
        #     for j in range(1, len(strs)):
        #         if i == len(strs[j]) or strs[0][i] != strs[j][i]:
        #             return strs[0][:i]
        # return strs[0]

        # SOLUTION NO 3

        index = 0
        for zipped in zip(*strs):
            if len(set(zipped)) != 1:
                break
            else:
                index += 1
        return strs[0][:index]
