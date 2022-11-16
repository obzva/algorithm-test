from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # MY SOLUTION - TIME LIMIT EXCEED

        # n = len(nums)
        #
        # heap = []
        # for i, num in enumerate(nums):
        #     heapq.heappush(heap, [-num, i])
        #
        # room = [-sys.maxsize] * n
        # while heap:
        #     count_k = k
        #     pop = heapq.heappop(heap)
        #     height, idx = -pop[0], pop[1]
        #     while idx < n and count_k:
        #         if room[idx] < height:
        #             room[idx] = height
        #         idx += 1
        #         count_k -= 1
        #
        # return room[k - 1:]

        # USING DEQUE

        # def q_operate(q: collections.deque, idx: int):
        #     if q and q[0] == idx - k:
        #         q.popleft()
        #     while q and nums[q[-1]] < nums[idx]:
        #         q.pop()
        #     q.append(idx)
        #
        # queue = collections.deque()
        # for i in range(k):
        #     q_operate(queue, i)
        # output = [nums[queue[0]]]
        # for i in range(k, len(nums)):
        #     q_operate(queue, i)
        #     output.append(nums[queue[0]])
        # return output

        # USING MEMO

        n = len(nums)
        memo_left, memo_right = nums[:], nums[:]

        left, right = [0] * n, [0] * n
        left[0], right[-1] = nums[0], nums[-1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            j = n - 1 - i
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        return [max(right[i], left[i + k - 1]) for i in range(n - k + 1)]
