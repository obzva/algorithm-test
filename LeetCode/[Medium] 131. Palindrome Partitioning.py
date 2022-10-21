from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # MY SOLUTION
        # if len(s) == 1:
        #     return [[s]]
        #
        # partition_candidate_num = len(s) - 1
        #
        # def combination(nums):
        #     result = [[]]
        #     for num in nums:
        #         result = result + [x + [num] for x in result]
        #     return result
        #
        # available_partitions = combination(range(partition_candidate_num))
        #
        # ans = []
        #
        # for partitions in available_partitions:
        #     if not partitions:
        #         if s == s[::-1]:
        #             ans.append([s])
        #         continue
        #
        #     tmp = []
        #     prev = 0
        #     for partition in partitions:
        #         if s[prev:partition + 1] == s[prev:partition + 1][::-1]:
        #             tmp.append(s[prev:partition + 1])
        #             prev = partition + 1
        #         else:
        #             break
        #     if len(tmp) == len(partitions):
        #         if s[prev:] == s[prev:][::-1]:
        #             tmp.append(s[prev:])
        #             ans.append(tmp)
        #
        # return ans

        # DFS
        result = []

        def is_palindrome(string):
            if string == string[::-1]:
                return True
            return False

        def dfs(string, path):
            nonlocal result
            if not string:
                result.append(path)
                return
            for i in range(1, len(string) + 1):
                if is_palindrome(string[:i]):
                    dfs(string[i:], path + [string[:i]])

        dfs(s, [])

        return result

