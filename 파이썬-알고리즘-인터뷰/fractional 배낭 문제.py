"""
Greedy
"""

from typing import *

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]


def fractional_knapsack(x: List[tuple[int]]):
    capacity = 15
    pack = []
    for c in x:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    total_value = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            total_value += capacity * p[0]
            break
    return total_value


fractional_knapsack(cargo)
