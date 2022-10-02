"""
Dynamic-programming
"""

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]


def zero_one_knapsack(x):
    capacity = 15
    pack = []
    for i in range(len(x) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif x[i - 1][1] <= c:
                pack[i].append(
                    max(
                        x[i - 1][0] + pack[i - 1][c - x[i - 1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1]


r = zero_one_knapsack(cargo)
