from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # MY SOLUTION - TIME LIMIT EXCEED
        # if not s:
        #     return True
        # for i in range(1, len(s) + 1):
        #     if s[:i] in wordDict:
        #         if self.wordBreak(s[i:], wordDict):
        #             return True
        # return False

        # USING MEMO
        memo = [False] * (len(s) + 1)
        memo[0] = True
        for i in range(len(s)):
            if memo[i]:
                for j in range(i, len(s)):
                    if s[i:j + 1] in wordDict:
                        memo[j + 1] = True
        return memo.pop()

