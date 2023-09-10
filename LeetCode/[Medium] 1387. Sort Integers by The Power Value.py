class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def step(n: int, prev: int) -> int:
            if n == 1:
                return prev

            if n % 2 == 0:
                return step(n // 2, prev + 1)
            else:
                return step(3 * n + 1, prev + 1)

        powers = [(step(num, 0), num) for num in range(lo, hi + 1)]
        heapq.heapify(powers)
        for _ in range(k - 1):
            heapq.heappop(powers)
        return heapq.heappop(powers)[1]

        # Time complexity
        ## iteration of power -> O(N * ?)
        ## building heap -> O(N)
        ## iteration of heapq method -> O(NlogN)
        ### O(N * ? + NlogN)

        # Space complexity
        ## heap -> O(N)
