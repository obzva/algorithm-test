import heapq
from typing import *


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # BUILD UP

        # BRUTE FORCE

        # positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        # edge_idx_map = {}
        # for i, x in enumerate(positions):
        #     edge_idx_map[x] = i
        #
        # heights = [0] * len(positions)
        # for left, right, height in buildings:
        #     left_idx, right_idx = edge_idx_map[left], edge_idx_map[right]
        #     for i in range(left_idx, right_idx):
        #         heights[i] = max(heights[i], height)
        #
        # answer = []
        # for i in range(len(heights)):
        #     curr_height = heights[i]
        #     curr_x = positions[i]
        #     if not answer or answer[-1][1] != curr_height:
        #         answer.append([curr_x, curr_height])
        # return answer

        # BRUTE FORCE - SWEEP LINE

        # positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        # answer = []
        # for position in positions:
        #     max_height = 0
        #     for left, right, height in buildings:
        #         if left <= position < right:
        #             max_height = max(max_height, height)
        #     if not answer or answer[-1][1] != max_height:
        #         answer.append([position, max_height])
        # return answer

        # SWEEP LINE WITH PRIORITY QUEUE

        # edges = []
        # for i, building in enumerate(buildings):
        #     edges.extend([[building[0], i], [building[1], i]])
        # edges.sort()
        #
        # answer = []
        # live = []
        #
        # idx = 0
        # while idx < len(edges):
        #     curr_x = edges[idx][0]
        #     while idx < len(edges) and curr_x == edges[idx][0]:
        #         building_idx = edges[idx][1]
        #         if buildings[building_idx][0] == curr_x:
        #             right = buildings[building_idx][1]
        #             height = buildings[building_idx][2]
        #             heapq.heappush(live, [-height, right])
        #
        #         while live and live[0][1] <= curr_x:
        #             heapq.heappop(live)
        #
        #         idx += 1
        #
        #     max_height = -live[0][0] if live else 0
        #
        #     if not answer or answer[-1][1] != max_height:
        #         answer.append([curr_x, max_height])
        #
        # return answer

        # SWEEP LINE WITH TWO PRIORITY QUEUES

        edges = []
        for i, building in enumerate(buildings):
            edges.extend([[building[0], building[2]], [building[1], -building[2]]])
        edges.sort()

        answer, live, past = [], [], []

        idx = 0
        while idx < len(edges):
            curr_x = edges[idx][0]
            while idx < len(edges) and curr_x == edges[idx][0]:
                height = edges[idx][1]
                if height > 0:
                    heapq.heappush(live, -height)
                else:
                    heapq.heappush(past, height)
                idx += 1
            while past and past[0] == live[0]:
                heapq.heappop(live)
                heapq.heappop(past)
            max_height = -live[0] if live else 0
            if not answer or answer[-1][1] != max_height:
                answer.append([curr_x, max_height])
        return answer
