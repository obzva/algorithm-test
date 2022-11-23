# IMPLEMENTATION OF BIT FOR RANGE SUM

class BIT:
    def __init__(self, data: list):
        self.size = len(data)
        self.data = [0] * self.size
        self.bit = [0] * (self.size + 1)
        for i in range(self.size):
            self.update(i, data[i])

    def update(self, idx: int, val: int):
        diff = val - self.data[idx]
        self.data[idx] = val
        idx += 1
        while idx <= self.size:
            self.bit[idx] += diff
            idx += idx & -idx

    def query(self, idx: int) -> int:
        idx += 1
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result
