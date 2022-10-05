import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # MY SOLUTION
        #
        # dic = {}
        # for i, char in enumerate(s):
        #     if char in dic:
        #         dic[char][1] += 1
        #     else:
        #         dic[char] = [i, 1]
        #
        # values = [x[0] for x in dic.values() if x[1] == 1]
        # if not values:
        #     return -1
        # return sorted(values)[0]

        # BETTER ONE

        dic = collections.defaultdict(int)
        for char in s:
            dic[char] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
