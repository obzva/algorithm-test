class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        for char in target:
            if char not in source_set:
                return -1

        n, m = len(source), len(target)
        i, j = 0, 0
        k = 1
        while j < m:
            if i == n:
                i = 0
                k += 1
            if source[i] == target[j]:
                j += 1
            i += 1

        return k

        # Time complexity
        ## constructing set -> O(N)
        ## iteration over target -> O(M)
        ## iteration to get k -> O(NM) at worst
        ### O(NM)

        # Space complexity
        ## set -> O(N)
        ### O(N)
