import collections
from typing import *


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # BRUTE FORCE - TIME LIMIT EXCEED

        # n = len(nums1)
        # answer = 0
        # for i in range(n):
        #     complement1 = -nums1[i]
        #     for j in range(n):
        #         complement2 = complement1 - nums2[j]
        #         for k in range(n):
        #             complement3 = complement2 - nums3[k]
        #             for l in range(n):
        #                 if nums4[l] == complement3:
        #                     answer += 1
        # return answer

        # OPTIMIZATION WITH HASHMAP

        # hashmap = collections.defaultdict(int)
        #
        # result = 0
        #
        # for num1 in nums1:
        #     for num2 in nums2:
        #         hashmap[num1 + num2] += 1
        #
        # for num3 in nums3:
        #     for num4 in nums4:
        #         if -num3 - num4 in hashmap:
        #             result += hashmap[-num3 - num4]
        #
        # return result

        # K SUM

        def get_sum_hashmap(lst_list: List[List[int]]) -> dict:
            res = collections.defaultdict(int)
            res[0] = 1
            for lst in lst_list:
                tmp = collections.defaultdict(int)
                for num in lst:
                    for total in res:
                        tmp[total + num] += res[total]
                res = tmp
            return res

        nums_list = [nums1, nums2, nums3, nums4]
        k = len(nums_list)
        left, right = get_sum_hashmap(nums_list[:k // 2]), get_sum_hashmap(nums_list[k // 2:])
        return sum(left[s] * right[-s] for s in left if -s in right)
