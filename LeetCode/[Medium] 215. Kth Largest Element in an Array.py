import heapq
from typing import *


class MinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i // 2

    def insert(self, item: int):
        self.items.append(item)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2
        right = left + 1
        smallest = idx
        if left <= len(self) and self.items[smallest] > self.items[left]:
            smallest = left
        if right <= len(self) and self.items[smallest] > self.items[right]:
            smallest = right
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self) -> int:
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ADT IMPLEMENTATION
        # min_heap = MinHeap()
        # for num in nums:
        #     min_heap.insert(-num)
        # for _ in range(k):
        #     answer = -min_heap.extract()
        # return answer

        # HEAPQ
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            answer = -heapq.heappop(nums)
        return answer
