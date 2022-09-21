"""
.pop(0) => .pop()
"""

import collections
from typing import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]
