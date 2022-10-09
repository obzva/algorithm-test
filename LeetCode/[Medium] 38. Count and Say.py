import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        # RECURSIVE
        # if n == 1:
        #     return '1'
        #
        # def count_say(prev: str, no: int) -> str:
        #     if no == n:
        #         return prev
        #
        #     if prev == '1':
        #         return count_say('11', 2)
        #
        #     say = ''
        #     count = 1
        #     for i in range(1, len(prev)):
        #         if prev[i] == prev[i - 1]:
        #             count += 1
        #         else:
        #             say += str(count) + prev[i - 1]
        #             count = 1
        #
        #         if i == len(prev) - 1:
        #             say += str(count) + prev[i]
        #
        #     return count_say(say, no + 1)
        #
        # return count_say('1', 1)

        # PYTHONIC - ITERTOOLS.GROUPBY
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        return s
