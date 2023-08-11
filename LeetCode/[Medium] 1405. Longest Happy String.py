from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, "a"))
        if b != 0:
            heappush(max_heap, (-b, "b"))
        if c != 0:
            heappush(max_heap, (-c, "c"))
        ans = ""
        while max_heap:
            remain1, char1 = heappop(max_heap)

            if (
                len(ans) >= 2 and ans[-1] == ans[-2] == char1
            ):  # if char1 is same as previous two
                if not max_heap:  # and there is no other choice
                    return ans
                remain2, char2 = heappop(max_heap)
                ans += char2
                remain2 += 1  # actually, count minus one
                if remain2 != 0:  # repush the second tuple to the heap
                    heappush(max_heap, (remain2, char2))
                heappush(max_heap, (remain1, char1))  # also repush the first one
                continue

            # if the first char can be added directly
            ans += char1
            remain1 += 1  # count minus one
            if remain1 != 0:
                heappush(max_heap, (remain1, char1))

        return ans

        # Time complexity
        ## heappush -> O(logN)
        ## heappop -> O(logN)
        ## iteration -> O(N)
        ### O(NlogN)

        # Space complexity
        ## heap -> O(N)
        ### O(N)
