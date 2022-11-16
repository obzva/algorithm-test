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

        # edges = []
        # for i, building in enumerate(buildings):
        #     edges.extend([[building[0], building[2]], [building[1], -building[2]]])
        # edges.sort()
        #
        # answer, live, past = [], [], []
        #
        # idx = 0
        # while idx < len(edges):
        #     curr_x = edges[idx][0]
        #     while idx < len(edges) and curr_x == edges[idx][0]:
        #         height = edges[idx][1]
        #         if height > 0:
        #             heapq.heappush(live, -height)
        #         else:
        #             heapq.heappush(past, height)
        #         idx += 1
        #     while past and past[0] == live[0]:
        #         heapq.heappop(live)
        #         heapq.heappop(past)
        #     max_height = -live[0] if live else 0
        #     if not answer or answer[-1][1] != max_height:
        #         answer.append([curr_x, max_height])
        # return answer

        # UNION FIND

        # edges = sorted(list(set([x for building in buildings for x in building[:2]])))
        # edges_mapping = {x: i for i, x in enumerate(edges)}
        #
        # buildings.sort(key=lambda x: -x[2])
        #
        # n = len(edges)
        # room = UnionFind(n)
        # heights = [0] * n
        #
        # for left_edge, right_edge, height in buildings:
        #     left_idx, right_idx = edges_mapping[left_edge], edges_mapping[right_edge]
        #     while left_idx < right_idx:
        #         left_idx = room.find(left_idx)
        #         if left_idx < right_idx:
        #             room.union(left_idx, right_idx)
        #             heights[left_idx] = height
        #             left_idx += 1
        #
        # answer = []
        # for i in range(n):
        #     if i == 0 or heights[i - 1] != heights[i]:
        #         answer.append([edges[i], heights[i]])
        #
        # return answer

        # class UnionFind:
        #     def __init__(self, n: int):
        #         self.root = list(range(n))
        #
        #     def find(self, x) -> int:
        #         if self.root[x] != x:
        #             self.root[x] = self.find(self.root[x])
        #         return self.root[x]
        #
        #     def union(self, x, y):
        #         self.root[x] = self.root[y]

        # DIVIDE AND CONQUER

        n = len(buildings)
        if n == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        def merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
            answer = []
            left_pos, right_pos = 0, 0
            left_prev_height, right_prev_height = 0, 0
            while left_pos < len(left) and right_pos < len(right):
                next_left_x, next_right_x = left[left_pos][0], right[right_pos][0]
                if next_left_x < next_right_x:
                    left_prev_height = left[left_pos][1]
                    curr_x = next_left_x
                    curr_y = max(left_prev_height, right_prev_height)
                    left_pos += 1
                elif next_left_x > next_right_x:
                    right_prev_height = right[right_pos][1]
                    curr_x = next_right_x
                    curr_y = max(left_prev_height, right_prev_height)
                    right_pos += 1
                else:
                    left_prev_height = left[left_pos][1]
                    right_prev_height = right[right_pos][1]
                    curr_x = next_left_x
                    curr_y = max(left_prev_height, right_prev_height)
                    left_pos += 1
                    right_pos += 1

                if not answer or answer[-1][1] != curr_y:
                    answer.append([curr_x, curr_y])

            while left_pos < len(left):
                answer.append(left[left_pos])
                left_pos += 1
            while right_pos < len(right):
                answer.append(right[right_pos])
                right_pos += 1

            return answer

        left_skyline = self.getSkyline(buildings[:n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])
        return merge(left_skyline, right_skyline)
