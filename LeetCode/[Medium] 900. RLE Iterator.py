class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.queue = collections.deque(encoding)

    def next(self, n: int) -> int:
        remainder = n
        while remainder > 0 and self.queue:
            cnt, val = self.queue[0], self.queue[1]
            if remainder > cnt:
                remainder -= cnt
                self.queue.popleft()
                self.queue.popleft()
            elif remainder < cnt:
                self.queue[0] -= remainder
                return val
            else:
                self.queue.popleft()
                self.queue.popleft()
                return val
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
