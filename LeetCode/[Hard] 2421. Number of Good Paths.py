class UnionFind:
    def __init__(self, size: int) -> None:
        self.groups = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, target: int) -> int:
        if self.groups[target] != target:
            self.groups[target] = self.find(self.groups[target])
        return self.groups[target]

    def union(self, x: int, y: int) -> bool:
        group_x, group_y = self.find(x), self.find(y)
        if group_x != group_y:
            if self.rank[group_x] > self.rank[group_y]:
                self.groups[group_y] = group_x
            if self.rank[group_x] < self.rank[group_y]:
                self.groups[group_x] = group_y
            else:
                self.groups[group_y] = group_x
                self.rank[group_x] += 1
            return True
        return False


class Solution:
    def calc_helper(self, n: int) -> int:
        return n * (n + 1) // 2

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        value_map = {}
        for i, val in enumerate(vals):
            if val in value_map:
                value_map[val].append(i)
            else:
                value_map[val] = [i]
        value_map = {k: v for k, v in sorted(value_map.items(), key=lambda x: x[0])}

        edge_map = {}
        for i in range(n):
            edge_map[i] = []
        for a, b in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)

        uf = UnionFind(n)
        res = 0
        for value in value_map.keys():
            for node in value_map[value]:
                for neighbor in edge_map[node]:
                    if vals[node] >= vals[neighbor]:
                        uf.union(node, neighbor)

            groups = {}
            for node in value_map[value]:
                group = uf.find(node)
                if group in groups:
                    groups[group] += 1
                else:
                    groups[group] = 1

            for group in groups:
                group_size = groups[group]
                res += self.calc_helper(group_size)

        return res

        # Time complexity
        ## constructing value_map -> O(NlogN)
        ## constructing edge_map -> O(N)
        ## iteration over edges -> O(N)
        ### O(NlogN)

        # Space complexity
        ## UnionFind, value_map, edge_map, groups -> O(N)
        ### O(N)
