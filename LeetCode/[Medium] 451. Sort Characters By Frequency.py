import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        cnt = collections.Counter(s)
        for elem in cnt.most_common():
            char, cnt = elem
            res = res + char * cnt
        return res
