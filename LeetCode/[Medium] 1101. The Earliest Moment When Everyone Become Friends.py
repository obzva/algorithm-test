# class Solution:
#     def earliestAcq(self, logs: List[List[int]], n: int) -> int:
#         logs.sort(key=lambda x: x[0])
#         acqs = set()
#         acqs_map = {}
#         for i in range(n):
#             acq = 1 << i
#             acqs.add(acq)
#             acqs_map[i] = acq
#         for timestamp, x, y in logs:
#             x_acq, y_acq = acqs_map[x], acqs_map[y]
#             union_acq = x_acq | y_acq
#             if union_acq != x_acq:
#                 acqs.remove(x_acq)
#                 acqs.remove(y_acq)
#                 acqs.add(union_acq)
#                 if len(acqs) == 1:
#                     return timestamp
#                 i, union_acq_copy = 0, union_acq
#                 while union_acq_copy:
#                     if union_acq_copy & 1:
#                         acqs_map[i] = union_acq
#                     i += 1
#                     union_acq_copy = union_acq_copy >> 1
#         return -1

#         # Time complexity
#         ## sort -> O(MlogM) for M logs
#         ## iteration for constructing acqs, acqs_map -> O(N)
#         ## iteration for logs -> O(MN)
#         ### O(MlogM + N + MN)

#         # Space complexity
#         ## acqs -> O(N)
#         ## acqs_map -> O(N)
#         ### O(N)


class UnionFind:
    def __init__(self, size) -> None:
        self.group = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, index: int) -> int:
        if index == self.group[index]:
            return index
        self.group[index] = self.find(self.group[index])
        return self.group[index]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> None:
        group_x = self.find(x)
        group_y = self.find(y)
        if group_x != group_y:
            if self.rank[group_x] > self.rank[group_y]:
                self.group[group_y] = group_x
            elif self.rank[group_x] < self.rank[group_y]:
                self.group[group_x] = group_y
            else:
                self.group[group_x] = group_y
                self.rank[group_y] += 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        union_find = UnionFind(n)
        count = n
        for timestamp, x, y in logs:
            if not union_find.is_connected(x, y):
                union_find.union(x, y)
                count -= 1
            if count == 1:
                return timestamp
        return -1

        # Time complexity
        ## sorting logs -> O(MlogM)
        ## constructing union find -> O(N)
        ## iteration <= O(M * N)
        ### O(MlogM + N + MN)

        # Space complexity
        ## constructing union find -> O(N)
