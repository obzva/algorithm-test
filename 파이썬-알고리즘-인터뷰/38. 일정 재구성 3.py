"""
loop
"""

import collections
from typing import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
