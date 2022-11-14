import collections
from typing import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        dic = collections.defaultdict(set)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x1 == x2:
                    a, b, c = 1, 0, -x1
                elif y1 == y2:
                    a, b, c = 0, 1, -y1
                else:
                    a, b, c = -1, (y1 - y2) / (x1 - x2), (x1 * y2 - x2 * y1) / (x1 - x2)

                dic[a, b, c].add((x1, y1))
                dic[a, b, c].add((x2, y2))

        return max(len(dic[key]) for key in dic)
