class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        acqs = set()
        acqs_map = {}
        for i in range(n):
            acq = 1 << i
            acqs.add(acq)
            acqs_map[i] = acq
        for timestamp, x, y in logs:
            x_acq, y_acq = acqs_map[x], acqs_map[y]
            union_acq = x_acq | y_acq
            if union_acq != x_acq:
                acqs.remove(x_acq)
                acqs.remove(y_acq)
                acqs.add(union_acq)
                if len(acqs) == 1:
                    return timestamp
                i, union_acq_copy = 0, union_acq
                while union_acq_copy:
                    if union_acq_copy & 1:
                        acqs_map[i] = union_acq
                    i += 1
                    union_acq_copy = union_acq_copy >> 1
        return -1
