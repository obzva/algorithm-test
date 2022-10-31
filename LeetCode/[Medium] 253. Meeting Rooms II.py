import heapq
from typing import *


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # MY SOLUTION
        # intervals.sort(key=lambda interval: [interval[0], interval[1]])
        # dic = collections.defaultdict(list)
        # for start, end in intervals:
        #     dic[start].append(end)
        # using = list()
        # max_room_cnt = 0
        # for start in list(dic.keys()):
        #     for end in dic[start]:
        #         new_using = []
        #         for i in range(len(using)):
        #             if using[i] > start:
        #                 new_using.append(using[i])
        #         new_using.append(end)
        #         using = new_using
        #         max_room_cnt = max(max_room_cnt, len(using))
        # return max_room_cnt

        # USING HEAP
        intervals.sort(key=lambda interval: interval[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)
