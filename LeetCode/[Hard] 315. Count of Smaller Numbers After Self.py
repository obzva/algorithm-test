from typing import *


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # USING SEGMENT TREE

        # min_val, max_val = min(nums), max(nums)
        # offset = -min_val
        # size = max_val - min_val + 1
        # tree = [0] * (size * 2)
        # answer = []
        #
        # def query(left: int, right: int) -> int:
        #     result = 0
        #     left, right = left + size, right + size
        #     while left <= right:
        #         if left % 2 == 1:
        #             result += tree[left]
        #             left += 1
        #         if right % 2 == 0:
        #             result += tree[right]
        #             right -= 1
        #         left, right = left // 2, right // 2
        #     return result
        #
        # def update(index: int):
        #     index += size
        #     tree[index] += 1
        #     while index > 0:
        #         index //= 2
        #         tree[index] = tree[index * 2] + tree[index * 2] + 1
        #
        # for num in reversed(nums):
        #     smaller_count = query(min_val + offset, num - 1 + offset)
        #     answer.append(smaller_count)
        #     update(num + offset)
        # return list(reversed(answer))

        # USING FENWICK TREE

        # min_val, max_val = min(nums), max(nums)
        # offset = -min_val + 1
        # size = max_val - min_val + 1
        # bi_tree = [0] * (size + 1)
        # answer = []
        #
        # def lsb(a: int):
        #     return a & -a
        #
        # def update(idx: int):
        #     while idx <= size:
        #         bi_tree[idx] += 1
        #         idx += lsb(idx)
        #
        # def query(idx: int) -> int:
        #     result = 0
        #     while idx > 0:
        #         result += bi_tree[idx]
        #         idx -= lsb(idx)
        #     return result
        #
        # for num in reversed(nums):
        #     answer.append(query(num + offset - 1))
        #     update(num + offset)
        # return list(reversed(answer))

        # USING MERGE SORT
        result = [0] * len(nums)

        def sort(arr: list):
            half = len(arr) // 2
            if half:
                left = sort(arr[:half])
                right = sort(arr[half:])
                for i in range(len(arr))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        result[left[-1][0]] += len(right)
                        arr[i] = left.pop()
                    else:
                        arr[i] = right.pop()
            return arr

        sort(list(enumerate(nums)))
        return result
